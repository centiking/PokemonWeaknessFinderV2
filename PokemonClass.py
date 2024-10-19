import json
from glob import glob

class Pokemon:
    def __init__(self, Pokemon):
        with open('Data.json') as json_data:
            self.data = json.load(json_data)
        self.Id = self.data[Pokemon]["Id"]
        self.Name = self.data[Pokemon]["Name"]
        self.Ability = self.data[Pokemon]["Ability"]
        self.Hp = self.data[Pokemon]["Hp"]
        self.Att = self.data[Pokemon]["Att"]
        self.Def = self.data[Pokemon]["Def"]
        self.SAtt = self.data[Pokemon]["S.Att"]
        self.SDef = self.data[Pokemon]["S.Def"]
        self.Spd = self.data[Pokemon]["Spd"]
        self.Weakness = self.data[Pokemon]["Weaknesses"]
        self.Types = self.data[Pokemon]["Types"]
        for Images in glob("PokemonImages/*.png"):
            if f"{self.Name}.png" == Images.replace("PokemonImages\\", ""):
                self.Image = Images
        self.Moves = self.data[Pokemon]["Moves"]


    def __str__(self):
        return self.Name

print(Pokemon("Abra").Id)