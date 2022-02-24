import os, json

class Player:
    def __init__(self, character_name):
        self.character_attributes = {
            'Username': character_name
        }

        with open('player.json', 'w') as attributes:
            json.dump(self.character_attributes, attributes)
            attributes.close()

    class Inventory:
        def __init__(self):
            try:
                file = open('inventory.json')
                inv = json.load(file)
                self.emeralds = inv['Emeralds']
                self.stone = inv['Stone']
                self.coal = inv['Coal']
                self.iron = inv['Iron']
                self.gold = inv['Gold']
                self.diamond = inv['Diamond']
                self.redstone = inv['Redstone']
                self.lapis = inv['Lapis'] 
                print("Inventory loaded successfully!")        
            except:
                self.emeralds = 0
                self.stone = 0
                self.coal = 0
                self.iron = 0
                self.gold = 0
                self.diamond = 0
                self.redstone = 0
                self.lapis = 0
        
        def DisplayInv(self):
            print("\nINVENTORY\n----------")
            self.inventory = {
                'Emeralds': self.emeralds,
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

        def Save(self):
            with open("inventory.json", "w") as inv:
                json.dump(self.inventory, inv)
                inv.close()
                print("Inventory saved!")

        # def Mine(self):
        #     self.coal += 10
        #     self.DisplayInv()

        def CommandHandle(self, command):
            self.commandlist = [
                "help - Display list of commands.",
                "exit - Exit the game.",
                "clear - Clear the terminal.",
                "mine - Mine blocks.",
                "inv - Display the inventory.",
                "save - Save your progress.",
                "pickstat - Display pickaxe stats.",
                "craft - Crafts a new pickaxe of user's choice."
            ]

            match (command):
                case "help":
                    self.commandlist = "\n".join(self.commandlist)
                    print(f"\nCommands:\n----------\n{self.commandlist}")
                case "exit":
                    self.Save()
                    exit(0)
                case "clear":
                    if os.name in ('nt', 'dos'):
                        os.system('cls')
                    else:
                        os.system('clear')
                case "mine":
                    pass
                    # self.Mine()
                case "inv":
                    self.DisplayInv()
                case "save":
                    self.Save()
                case "pickstat":
                    pass
                case "craft":
                    pass
                case _:
                    print(f"'{command}' is an unknown command")

    class Pickaxe:
        def __init__(self, material, cost, durability, efficiency, fortune, mending, unbreaking):
            self.material = material
            self.cost = cost
            self.durability = durability
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking

            self.materials = [
                "[1] Wooden Pickaxe",
                "[2] Stone Pickaxe",
                "[3] Iron Pickaxe",
                "[4] Gold Pickaxe",
                "[5] Diamond Pickaxe",
            ]

            try:
                file = open("picktype.json", "r")
                pick = json.load(file)
                self.type = {
                    "Material": pick['Material'],
                    "Durability": pick['Durability'],
                    "Efficiency": pick['Efficiency'],
                    "Fortune": pick['Fortune'],
                    "Mending": pick['Mending'],
                    "Unbreaking": pick['Unbreaking']
                }
                print("Pickaxe loaded successfully!")
            except:
                self.type = {
                    "Material": self.material,
                    "Durability": self.durability,
                    "Efficiency": self.efficiency,
                    "Fortune": self.fortune,
                    "Mending": self.mending,
                    "Unbreaking": self.unbreaking
                }
                print("Error loading pickaxe...")

        def SavePickaxe(self):
            with open("picktype.json", "w") as pick:
                json.dump(self.type, pick)
                pick.close()
                print("Pickaxe saved!")

        def DisplayPick(self):
            for item, value in self.type.items():
                print(f"{item}: {value}")

        def HandleEnchantments(self, enchantment):
            pass