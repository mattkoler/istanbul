
def tile_num_to_name(number):
    """Takes in the tile's original (blue) number and returns the name"""
    tiles = {
        1:'Wainwright',
        2:'Fabric Warehouse',
        3:'Spice Warehouse',
        4:'Fruit Warehouse',
        5:'Post Office',
        6:'Caravansary',
        7:'Fountain',
        8:'Black Market',
        9:'Tea House',
        10:'Small Market',
        11:'Large Market',
        12:'Police Station',
        13:"Sultan's Palace",
        14:'Small Mosque',
        15:'Great Mosque',
        16:'Gemstone Dealer'
    }
    return tiles[number]
