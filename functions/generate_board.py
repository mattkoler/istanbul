import random

def generate_board(order='default'):
    """Generates a board based on the order specified
    None/Default - Ascending order
    Shortest - Tiles with synergies placed close together
    Farthest - Tiles with synergies placed far apart
    Random - Random layout that follows  book rules
    Balanced - A random layout with more rules to help balance
    Random Rules:
        1. Fountain(7) one of the 4 center tiles
        2. Black Market(8) and Tea House(9) >= 3 tiles away
    Balanced Rules:
        1. Caravansery (6) and Fountain (7) must be in the center 4 tiles
        2. Tea House (9) must be one of the corners
        3. Black Market (8) and Gemstone Dealer (16) at least 3 away from Tea House
        4. At least 4 of the following 1-2 away from the Fountain
            - Fabric (2) / Spice (3) / Fruit (4) Warehouses
            - Post Office (5)
            - Black Market (8)
            - Tea house (9)
            - Police Station (12)
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

    elif order.lower() == 'balanced':
        #generate a placeholder list to put our tile indices into
        layout = [False,]*16
        
        
        #pick a center tile for the fountain (7) and Caravansery (6) which could be 5,6,9,10
        center = [5,6,9,10]
        random.shuffle(center)
        fountain = center[0]
        caravansery = center[1]
        layout[fountain] = 7
        layout[caravansery] = 6

        #pick a corner tile for the Tea House (9)
        corners = [0,3,12,15]
        random.shuffle(corners)
        tea_house = corners[0]
        layout[tea_house] = 9

        #set tiles that are at least 3 away from Tea House for Black Market (8) and Gemstone Dealer (16)
        if tea_house == 0:
            dist_three = [3,6,7,9,10,11,12,13,14,15]
        elif tea_house == 3:
            dist_three = [0,4,5,8,9,10,12,13,14,15]
        elif tea_house == 12:
            dist_three = [0,1,2,3,5,6,7,10,11,15]
        elif tea_house == 15:
            dist_three = [0,1,2,3,4,5,6,8,9,12]
        else:
            print('Something went wrong',tea_house)
        
        #remove the values we chose from the Fountain and Caravansary
        try:
            dist_three.remove(center[0])
        except ValueError:
            pass

        try:
            dist_three.remove(center[1])
        except ValueError:
            pass
        
        #shuffle and set the Black Market (8) and Gemstone Dealer (16) to those tiles
        random.shuffle(dist_three)
        black_market = dist_three[0]
        gemstone_dealer = dist_three[1]
        layout[black_market] = 8
        layout[gemstone_dealer] = 16
        
        #set remaining tiles, shuffle them, and make sure at least 4 special are <= 2 dist from Fountain
        while True:
            test_layout = list(layout)
            remaining = [1,2,3,4,5,10,11,12,13,14,15]
            random.shuffle(remaining)
            special = 0
            if abs(black_market//4 - fountain//4) + abs(black_market%4 + fountain%4) <= 2:
                special += 1
            if abs(tea_house//4 - fountain//4) + abs(tea_house%4 + fountain%4) <= 2:
                special += 1
            for i in range(16):
                if test_layout[i] != False:
                    continue
                tile = remaining.pop()
                if tile in [2,3,4,5,12] and abs(i//4 - fountain//4) + abs(i%4 - fountain%4) <= 2:
                    special += 1
                test_layout[i] = tile
            if special >= 4:
                layout = list(test_layout)
                break
        
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