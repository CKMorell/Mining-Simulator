import os
from pickaxe import Pickaxe

class Player:
    class Inventory:
        def __init__(self):
            self.money = 0
            self.stone = 0
            self.coal = 0
            self.iron = 0
            self.gold = 0
            self.diamond = 0
            self.redstone = 0
            self.lapis = 0
        
        def DisplayInv(self):
            print("INVENTORY\n----------")
            self.inventory = {
                'Money': f"${self.money}\n",
                'Stone': self.stone,
                'Coal': self.coal,
                'Iron': self.iron,
                'Gold': self.gold,
                'Diamond': self.diamond,
                'Redstone': self.redstone,
                'Lapis': self.lapis
            }

            for item, value in self.inventory.items():
                print(f"{item}: {value}")

        def CommandHandle(self, command):
            self.commandlist = [
                "help",
                "exit",
                "clear"
            ]

            # Handles command line input
            if (command == self.commandlist[0]):
                self.commandlist = "\n".join(self.commandlist)
                print(f"\nCommands:\n----------\n{self.commandlist}")
            elif (command == self.commandlist[1]):
                exit(0)
            elif (command == self.commandlist[2]):
                if os.name in ('nt', 'dos'):
                    os.system('cls')
                else:
                    os.system('clear')
            else:
                print(f"'{command}' is an unknown command.\n")
