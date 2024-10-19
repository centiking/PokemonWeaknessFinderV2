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
    datas = json.load(json_data)


def findPokemon(pokemon):
    global datas
    Nums = ["1","2","3","4","5","6","7","8","9"]
    FullPokemon = datas[pokemon]
    Moves = {}
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        # Add other headers as needed
    }

    # Introduce a random delay
    # time.sleep(random.uniform(1, 3))

    response = requests.get(f"https://pokemondb.net/move/all", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for Move in FullPokemon["Moves"]:
        A = soup.find_all("a", {"class": "ent-name"})
        for i in A:
            if Move == i.text:
                Moves[Move] = [i.parent.parent.find_all("a", {"class": "type-icon"})[0].text,i.parent.parent.find_all("td", {"class": "cell-long-text"})[0].text]

    FullPokemon["Moves"] = Moves
    AllPokemon[pokemon] = FullPokemon
    print(f"{pokemon} finished")

data = list(datas.keys())

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(findPokemon, data)


with open("Data.json", "w", encoding='utf-8') as outfile:
    json.dump(AllPokemon, outfile, ensure_ascii=False, indent=4)



