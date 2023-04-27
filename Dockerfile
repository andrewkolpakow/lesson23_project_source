FROM python:3.10-slim

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt
#Копируем requirements и устанавливаем - это первый слой контейнера Docker

COPY . .

CMD ["sh", "entrypoint.sh"]