# Imports
import json
from player import Player

# Player init
try:
    file = open('player.json')
    data = json.load(file)
    character_name = data['Username']
except:
    character_name = input("Enter your character name: ")

Player = Player(character_name)

# Inventory init
Inventory = Player.Inventory()

# Pickaxe init
Pickaxe = Player.Pickaxe("Wooden", 1, 59, 0, 0, 0, 0)

# Game loop
running = True

def main():
    Inventory.DisplayInv()

    while running:
        command = input(f"\n{character_name}~> ")
        if (command == "save"):
            Pickaxe.SavePickaxe()
            Inventory.CommandHandle(command)
        elif (command == "exit"):
            Pickaxe.SavePickaxe()
            Inventory.CommandHandle(command)
        elif (command == "picktype"):
            Pickaxe.DisplayPick()
            Inventory.CommandHandle(command)
        else:
            Inventory.CommandHandle(command)

        # Inventory.DisplayInv()

main()
