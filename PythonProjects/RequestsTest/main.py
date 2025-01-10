import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5e28f0b51a597c610e5438ccddd30ac2'
HEADER = {'Content-Type':'application/JSON', 'trainer_token': TOKEN}
TRAINER_ID = '14983'

body_create_pokemon = { # боди для создания покемона
    "name": "generate", 
    "photo_id": -1
    }

body_new_name_pokemon = { # боди для смены имени покемона
    "pokemon_id": "188558",
    "name": "generate",
    "photo_id": -1
}

body_pokemon_in_pokeball = { # боди для ловли покемона в покеболл
    "pokemon_id": "188558"
}

# запрос на создание покемона
response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
pokemon_id = response_create_pokemon.json()['id']
print(response_create_pokemon.text)


# запрос cмена имени покемона
response_new_name_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name_pokemon)
print(response_new_name_pokemon.text)

# запрос на поимку покемона в покеболл
response_pokemon_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_in_pokeball)
print(response_pokemon_in_pokeball.text)