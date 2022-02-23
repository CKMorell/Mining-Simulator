# Imports
import json
from pickaxe import Pickaxe
from player import Player

# Inventory init
Inventory = Player.Inventory()

# Pickaxe init
WoodenPick = Pickaxe.WoodenPick(0, 0, 0, 0)
StonePick = Pickaxe.StonePick(0, 0, 0, 0)
IronPick = Pickaxe.IronPick(0, 0, 0, 0)
GoldPick = Pickaxe.GoldenPick(0, 0, 0, 0)
DiamondPick = Pickaxe.DiamondPick(0, 0, 0, 0)
NetheritePick = Pickaxe.NetheritePick(0, 0, 0, 0)

running = True

def main():
    Inventory.DisplayInv()

    while running:
        command = input("---> ")
        Inventory.CommandHandle(command)
        # Inventory.DisplayInv()

main()
