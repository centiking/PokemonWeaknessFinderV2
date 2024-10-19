from customtkinter import CTkLabel
from PokemonClass import Pokemon as Pk
import tkinter as tk
from tkinter import Tk, StringVar
import customtkinter as ctk
import json
import os
from PIL import Image

with open("Data.json") as f:
    PokemonNames = list(json.load(f).keys())

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Pokemon Weakness Finder")
root.iconbitmap("ball.ico")

Image_Frame = ctk.CTkFrame(root, bg_color="#1A1A1A", fg_color="#1A1A1A")
Image_Frame.grid(column=1,row=0,pady=5)

Top_Frame = ctk.CTkFrame(root)
Top_Frame.grid(column=1,row=1,padx=5,pady=5)

Level_MoveBar = ctk.CTkScrollableFrame(root, label_text="Pokemon Level Up Moves")
Level_MoveBar.grid(column=0,pady=5,padx=5,row=0, rowspan=6,sticky="nsew")

Middle_Frame = ctk.CTkFrame(root)
Middle_Frame.grid(column=1,row=2,padx=5,pady=5)

Info = ctk.CTkLabel(Middle_Frame, text="", font=("Arial", 16))
Info.grid(column=1,row=3,padx=5,pady=5)

Lower_Frame = ctk.CTkFrame(root)
Lower_Frame.grid(column=1,row=4,padx=5,pady=5)

Bottom_Grid = ctk.CTkFrame(root)
Bottom_Grid.grid(column=1,row=5,padx=5,pady=5)

ctk.CTkLabel(Top_Frame, text="Pokemon Weakness Finder", font=("Arial", 25)).grid(column=0, row=0, columnspan=2, padx=5, pady=5)
PokemonName = ctk.CTkComboBox(Top_Frame, values=PokemonNames)
PokemonName.grid(columnspan=2, padx=5, pady=5)

def FilterPokemon():
    Filtered = []
    text = PokemonName.get().lower()
    for I in PokemonNames:
        if text in I.lower():
            Filtered.append(I)
    if Filtered:
        PokemonName.configure(values=Filtered)
    else:
        PokemonName.configure(values=PokemonNames)
def SearchPokemon():
    Color = ["#aa9", "#f42", "#39f", "#fc3", "#7c5", "#6cf", "#b54", "#a59", "#db5"]
    Color2 = ["#89f", "#f59", "#ab2", "#ba6", "#66b", "#76e", "#754", "#aab", "#e9e"]
    unicode_to_regular = {
        "½": "1/2",
        "⅓": "1/3",
        "¼": "1/4",
        "¾": "3/4",
    }
    def create_label_in_frame(parent, row, column, text,Color, Pokemon):
            frame = ctk.CTkFrame(parent, width=50, height=50,corner_radius=5)
            frame.grid(row=row, column=column, padx=5, pady=5)
            label = ctk.CTkLabel(frame, text=text, width=50, height=50, font=("Arial", 25),text_color="black",fg_color=Color[w],corner_radius=5)
            label.pack()

            frame = ctk.CTkFrame(parent, width=50, height=50, corner_radius=5)
            frame.grid(row=row+1, column=column, padx=5, pady=5)

            Pokemon.Weakness[text] = Pokemon.Weakness[text].replace("Ã‚Â", "")
            if Pokemon.Weakness[text] == "1":
                label = ctk.CTkLabel(frame, text=Pokemon.Weakness[text], width=50, height=50, font=("Arial", 25), text_color="black",fg_color="grey", corner_radius=5)
                label.pack()
            elif Pokemon.Weakness[text] == "0":
                label = ctk.CTkLabel(frame, text=Pokemon.Weakness[text], width=50, height=50, font=("Arial", 25),
                                     text_color="yellow", fg_color="black", corner_radius=5)
                label.pack()
            else:
                regular_fraction_str = unicode_to_regular.get(Pokemon.Weakness[text])
                if regular_fraction_str:
                    label = ctk.CTkLabel(frame, text=Pokemon.Weakness[text], width=50, height=50, font=("Arial", 25), text_color="black",fg_color="red", corner_radius=5)
                    label.pack()
                else:
                    label = ctk.CTkLabel(frame, text=Pokemon.Weakness[text], width=50, height=50, font=("Arial", 25),
                                         text_color="black", fg_color="green", corner_radius=5)
                    label.pack()



            label.pack()
    text = PokemonName.get().lower()

    for I in PokemonNames:
        if text in I.lower():
            Pokemon = Pk(I)
    # Assuming Pokemon.Weakness is a dictionary
    keys = list(Pokemon.Weakness.keys())

    # Track the number of keys used
    used_keys_count = 0

    for widget in Bottom_Grid.winfo_children():
        widget.destroy()
    # First, fill the top row
    for h in range(2):
        for w in range(9):
            if h == 0:
                # Calculate the index based on the current loop iteration
                index = h * 9 + w
                if index < len(keys):
                    # Pass one key at a time
                    create_label_in_frame(Bottom_Grid, h, w, keys[index],Color,Pokemon)
                    used_keys_count += 1

    # Now, handle the remaining keys for the bottom row
    remaining_keys = keys[used_keys_count:]

    for w in range(len(remaining_keys)):
        # Place remaining keys in the second row
        create_label_in_frame(Bottom_Grid, 2, w, remaining_keys[w],Color2,Pokemon)

    Info.configure(text=f"Ability:{Pokemon.Ability}|Hp:{Pokemon.Hp} | Attack:{Pokemon.Att} | Defense:{Pokemon.Def} | Sp.Atk:{Pokemon.SAtt} | Sp.Def:{Pokemon.SDef} | Speed:{Pokemon.Spd}")
    for widget in Lower_Frame.winfo_children():
        widget.destroy()
    for i,v in enumerate(Pokemon.Types):
        fg = {
            "Fire": "#f42",
            "Flying": "#89f",
            "Normal": "#aa9",
            "Water": "#39f",
            "Electric": "#fc3",
            "Grass": "#7c5",
            "Ice": "#6cf",
            "Fighting": "#b54",
            "Poison": "#a59",
            "Ground": "#db5",
            "Psychic": "#f59",
            "Bug": "#ab2",
            "Rock": "#ba6",
            "Ghost": "#66b",
            "Dragon": "#76e",
            "Dark": "#754",
            "Steel": "#aab",
            "Fairy": "#e9e",
        }
        fg = fg.get(v)
        ctk.CTkLabel(Lower_Frame, text=f"{Pokemon.Types[v]}",text_color="white" ,font=("Arial", 24), fg_color=fg,width=50, height=50, corner_radius=5).grid(column=i, row=0, padx=5, pady=5)

        for widget in Image_Frame.winfo_children():
            widget.destroy()
        your_image = ctk.CTkImage(light_image=Image.open(os.path.join(Pokemon.Image)), size=(150, 150))
        ctk.CTkLabel(master=Image_Frame, image=your_image, text='', corner_radius=50).grid(column=0, row=0)
        Level_MoveBar.configure(Values=Pokemon.Moves)


PokemonName.bind("<Key>", lambda x: root.after(1, FilterPokemon))
PokemonName.bind("<Return>", lambda x: root.after(1, SearchPokemon))
root.mainloop()
