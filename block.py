# class Blocks:
#     class Stone:
#         def __init__(self):
#             pass

#     class Coal:
#         def __init__(self):
#             pass

#     class Iron:
#         def __init__(self):
#             pass

#     class Gold:
#         def __init__(self):
#             pass

#     class Diamond:
#         def __init__(self):
#             pass

#     class Redstone:
#         def __init__(self):
#             pass

#     class Lapis:
#         def __init__(self):
#             pass
class Block:
    def __init__(self, material, rate, value, type):
        self.material = material # Block material (i.e., stone)
        self.rate = rate # Rate of generation out of 100
        self.value = value # How much currency it returns
        self.type = type # 1 - 3 denoting which pickaxes can mine the block
