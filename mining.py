# Imports
from glob import glob
import json, random
from math import floor
from player import Player
from block import Block

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
pickaxes = {
    "Wooden": Player.Pickaxe("Wooden", 1, 59, 0, 0, 0, 0),
    "Stone": Player.Pickaxe("Stone", 1, 131, 0, 0, 0, 0),
    "Iron": Player.Pickaxe("Iron", 1, 250, 0, 0, 0, 0),
    "Gold": Player.Pickaxe("Gold", 1, 32, 0, 0, 0, 0),
    "Diamond": Player.Pickaxe("Diamond", 1, 1561, 0, 0, 0, 0)
}

CurrentPickaxe = pickaxes["Wooden"]
Pickaxe = CurrentPickaxe

# Block init
Stone = Block("stone", 90, 75, 1)
Coal = Block("coal", 35, 30, 1)
Iron = Block("iron", 90, 20, 2)
Gold = Block("gold", 90, 15, 3)
Diamond = Block("diamond", 90, 5, 3)
Redstone = Block("redstone", 90, 10, 3)
Lapis = Block("lapis", 90, 15, 3)

# Game loop
running = True

def mine():
    StonePercentage = floor((random.random() * Stone.rate))
    CoalPercentage = floor((random.random() * Coal.rate))
    IronPercentage = floor((random.random() * Iron.rate))
    GoldPercentage = floor((random.random() * Gold.rate))
    DiamondPercentage = floor((random.random() * Diamond.rate))
    RedstonePercentage = floor((random.random() * Redstone.rate))
    LapisPercentage = floor((random.random() * Lapis.rate))

    # Inventory.stone += StonePercentage
    # Inventory.coal += CoalPercentage
    # Inventory.iron += IronPercentage
    # Inventory.gold += GoldPercentage
    # Inventory.diamond += DiamondPercentage
    # Inventory.redstone += RedstonePercentage
    # Inventory.lapis += LapisPercentage
    
    Inventory.DisplayInv()

def craft(choice):
    # WoodenPick = Player.Pickaxe("Wooden", 1, 59, 0, 0, 0, 0)
    # StonePick = Player.Pickaxe("Stone", 1, 131, 0, 0, 0, 0)
    # IronPick = Player.Pickaxe("Iron", 1, 250, 0, 0, 0, 0)
    # GoldPick = Player.Pickaxe("Gold", 1, 32, 0, 0, 0, 0)
    # DiamondPick = Player.Pickaxe("Diamond", 1, 1561, 0, 0, 0, 0)
    global CurrentPickaxe, pickaxes, Pickaxe

    match (choice):
        case 1:
            try:
                CurrentPickaxe = pickaxes["Stone"]
                with  open("picktype.json", "w") as file:
                    data = json.dump(Pickaxe, file)
                    file.close()
            except:
                print("Error crafting")
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            print("Error! Not a valid choice!")

def main():
    global Pickaxe
    Inventory.DisplayInv()

    while running:
        command = input(f"\n{character_name}~> ")
        if (command == "save"):
            Pickaxe.SavePickaxe()
            Inventory.CommandHandle(command)
        elif (command == "exit"):
            Pickaxe.SavePickaxe()
            Inventory.CommandHandle(command)
        elif (command == "pickstat"):
            Pickaxe.DisplayPick()
            Inventory.CommandHandle(command)
        elif (command == "mine"):
            mine()
            Inventory.CommandHandle(command)
        elif (command == "craft"):
            print("\n")
            for i in Pickaxe.materials:
                print(i)

            print("What would you like to craft? Select number.\n")
            choice = int(input("Craft~> "))
            craft(choice)
        else:
            Inventory.CommandHandle(command)

main()
