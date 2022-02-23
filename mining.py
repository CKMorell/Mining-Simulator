# Imports
import json
from pickaxe import Pickaxe
from player import Player

# Inventory init
Inventory = Player.Inventory()

# Pickaxe init
WoodenPick = Pickaxe.WoodenPick(False, False, False, False)
StonePick = Pickaxe.StonePick(False, False, False, False)
IronPick = Pickaxe.IronPick(False, False, False, False)
GoldPick = Pickaxe.GoldenPick(False, False, False, False)
DiamondPick = Pickaxe.DiamondPick(False, False, False, False)
NetheritePick = Pickaxe.NetheritePick(False, False, False, False)

running = True

# def commandhandler(command):
#     if (command == "test"):
#         Inventory.coal += 10
#         Inventory.DisplayInv()

def main():
    Inventory.DisplayInv()

    while running:
        command = input("---> ")
        Inventory.CommandHandle(command)
        # Inventory.DisplayInv()

main()
