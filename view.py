from typing import Union, Tuple, Dict, List

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema, BatchRequestSchema

FILE_NAME = 'data/apache_logs.txt'

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perfrom_query() -> Union[Response, Tuple[Response, int]]:
    #Принимаем запрос от пользователя
    data: Dict[str, Union[List[dict], str]] = request.json
    #Обрабатываем запрос, валидируем значения
    try:
        validate_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400


    result = None
    for query in validate_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result
        )

    return jsonify(result)