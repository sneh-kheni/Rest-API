import requests

url = 'https://pokeapi.co/api/v2/'

def get_info(name):
    main_url = f'{url}/pokemon/{name}'
    response = requests.get(main_url)
    if response.status_code==200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("failed to retrieve data!!")

while True:

    name = input('enter the name of pokemon: ')
    pokemon_info = get_info(name)
    if name =='quit':
        break
    if pokemon_info:
        print(f'{pokemon_info['name']}')
        print(f'{pokemon_info['height']}')
        print(f'{pokemon_info['weight']}')

