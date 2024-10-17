import requests
from bs4 import BeautifulSoup
import json
import random

import time
import re
from concurrent.futures import ThreadPoolExecutor
AllPokemon = {}

# List of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    # Add more user agents
]

# Load data from JSON
with open('Data.json') as json_data:
    data = json.load(json_data)


def findPokemon(pokemon):
    global data
    FullPokemon = {}
    Weakness = {}
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        # Add other headers as needed
    }

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    response = requests.get(f"https://pokemondb.net/sprites", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("img", {"class": "img-fixed icon-pkmn", "alt":f"{pokemon}"}).get("src")
    img_data = requests.get(table).content
    with open(f'PokemonImages\\{pokemon}.png', 'wb') as handler:
        handler.write(img_data)

data = list(data.keys())
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(findPokemon, data)