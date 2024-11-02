import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados, a view da miha API
    name: str
    type: str

    class Config:
        orm_mode = True

URL = 'https://pokeapi.co/api/v2/pokemon/25'


def capturar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    data_types = data['types']
    list_type = []
    for type_list in data_types:
        list_type.append(type_list['type']['name'])
    types = ', '.join(list_type)
    return PokemonSchema(name=data['name'], type=types)


if __name__ == "__main__":
    print(capturar_pokemon(id=55))
    print(capturar_pokemon(id=47))
