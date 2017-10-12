import random

def generate_board(order='default'):
    """Generates a board based on the order specified
    None/Default - Ascending order
    Shortest - Tiles with synergies placed close together
    Farthest - Tiles with synergies placed far apart
    Random - Random layout that still complies with rules
    Rules:
        1. Fountain(7) one of the 4 center tiles
        2. Black Market(8) and Tea House(9) >= 3 tiles away
    """
    #tiles in ascending (red numbers) order
    tiles = { 
            1:"Wainwright",
            2:"Fabric Warehouse",
            3:"Spice Warehouse",
            4:"Fruit Warehouse",
            5:"Post Office",
            6:"Caravansary",
            7:"Fountain",
            8:"Black Market",
            9:"Tea house",
            10:"Small Market",
            11:"Large Market",
            12:"Police Station",
            13:"Sultan's Palace",
            14:"Small Mosque",
            15:"Great Mosque",
            16:"Gemstone Dealer"
            }
    if order.lower() == 'default':
        layout = list(range(1,17))
    elif order.lower() == 'shortest':
        #tiles in blue number order
        layout = [15, 5, 2, 14, 4, 12, 7, 3, 8, 6, 11, 9, 13, 10, 1, 16]
    elif order.lower() == 'farthest':
        #tiles in green number order
        layout = [16, 2, 8, 11, 15, 7, 6, 4, 3, 5, 12, 1, 10, 9, 14, 13]
    elif order.lower() == 'random':
        #generate a placeholder list to put our tile indices into
        layout = [False,]*16
        
        #pick a center tile for the fountain (7) which could be 5,6,9,10
        if random.randint(0,1) == 0:
            layout[random.randint(5,6)] = 7
        else:
            layout[random.randint(9,10)] = 7
        
        #pick an unused tile for the Black Market (8)
        black_market = random.randint(0,15)
        while layout[black_market] != False:
            black_market = random.randint(0,15)
        layout[black_market] = 8
        
        #pick an unused tile for the Tea House and make sure it is >=3 away
        while True:
            tea_house = random.randint(0,15)
            if layout[tea_house] != False:
                continue
            if abs(black_market//4 - tea_house//4) + abs (black_market%4 - tea_house%4) >= 3:
                break
        layout[tea_house] = 9
        
        remaining = [1,2,3,4,5,6,10,11,12,13,14,15,16]
        random.shuffle(remaining)
        for i in range(16):
            if layout[i] != False:
                continue
            layout[i] = remaining.pop()
        
    else: 
        print("Bad input for generate_board:",order)
        return None
    
    #combine our indices in layouts with the tile dict to get an ordered list of tiles
    order = []
    for i in layout:
        order.append(tiles[i])
        
    #print out our tiles in a 4x4 grid in a nice text based way    
    offset = 0
    print('+-------------------+-------------------+-------------------+-------------------+')
    for row in range(4):
        line = '| %s| %s| %s| %s|' % ("{:<18}".format(order[offset]), "{:<18}".format(order[1+offset]), "{:<18}".format(order[2+offset]), "{:<18}".format(order[3+offset]))
        offset += 4
        print(line)
        print('+-------------------+-------------------+-------------------+-------------------+')