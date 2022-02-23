class Pickaxe:
    class WoodenPick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Wooden"
            self.cost = 100
            self.durability = 59
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    class StonePick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Stone"
            self.cost = 200
            self.durability = 131
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    class IronPick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Iron"
            self.cost = 300
            self.durability = 250
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    class GoldenPick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Gold"
            self.cost = 400
            self.durability = 32
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    class DiamondPick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Diamond"
            self.cost = 500
            self.durability = 1561
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    class NetheritePick:
        def __init__(self, efficiency, fortune, mending, unbreaking):
            self.material = "Netherite"
            self.cost = 600
            self.durability = 2031
            self.efficiency = efficiency
            self.fortune = fortune
            self.mending = mending
            self.unbreaking = unbreaking
            self.enchantments = [efficiency, fortune, mending, unbreaking]

    def HandleEnchantments(self):
        pass
