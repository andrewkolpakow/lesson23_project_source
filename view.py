from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from models import RequestSchema

FILE_NAME = 'data/apache_logs.txt'

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perfrom_query():
    #Принимаем запрос от пользователя
    data = request.json
    #Обрабатываем запрос, валидируем значения
    try:
        validate_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400


