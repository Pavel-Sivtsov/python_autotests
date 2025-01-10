import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5e28f0b51a597c610e5438ccddd30ac2'
HEADER = {'Content-Type':'application/JSON', 'trainer_token': TOKEN}
TRAINER_ID = '14983'

def test_trainer_status_code(): # тест на получение ответа со статусом 200
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200


def test_trainer_status_code(): # Тест на получение id тренера
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.json()['data'][0]["id"] == '14983'