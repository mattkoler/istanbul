import random
import tile as t

def generate_board(num_players, order='default'):
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
    tiles = [
        t.Wainwright(num_players),   #0
        t.FabricWarehouse(),         #1
        t.SpiceWarehouse(),          #2
        t.FruitWarehouse(),          #3
        t.PostOffice(),              #4
        t.Caravansary(),             #5
        t.Fountain(),                #6
        t.BlackMarket(),             #7
        t.TeaHouse(),                #8
        t.SmallMarket(),             #9
        t.LargeMarket(),             #10
        t.PoliceStation(),           #11
        t.SultansPalace(num_players),#12
        t.SmallMosque(num_players),  #13
        t.GreatMosque(num_players),  #14
        t.GemstoneDealer(num_players)#15
    ]

    if order.lower() == 'default':
        return tiles
    elif order.lower() == 'shortest':
        #tiles in blue number order
        layout = [14, 4, 1, 13, 3, 11, 6, 2, 7, 5, 10, 8, 12, 9, 0, 15]
        shortest = []
        for tile in layout:
            shortest.append(tiles[tile])
        return shortest
    elif order.lower() == 'farthest':
        #tiles in green number order
        layout = [15, 1, 7, 10, 14, 6, 5, 3, 2, 4, 11, 0, 9, 8, 13, 12]
        farthest = []
        for tile in layout:
            farthest.append(tiles[tile])
        return farthest
    elif order.lower() == 'random':
        #generate a placeholder list to put our tile indices into
        rand = [False,]*16
        
        #pick a center tile for the fountain which could be loc 5,6,9,10
        if random.randint(0,1) == 0:
            rand[random.randint(5,6)] = tiles[6]
        else:
            rand[random.randint(9,10)] = tiles[6]
        
        #pick an unused tile for the Black Market 
        black_market = random.randint(0,15)
        while rand[black_market] != False:
            black_market = random.randint(0,15)
        rand[black_market] = tiles[7]
        
        #pick an unused tile for the Tea House and make sure it is >=3 away
        while True:
            tea_house = random.randint(0,15)
            if rand[tea_house] != False:
                continue
            if abs(black_market//4 - tea_house//4) + abs (black_market%4 - tea_house%4) >= 3:
                break
        rand[tea_house] = tiles[8]
        
        remaining = [0,1,2,3,4,5,9,10,11,12,13,14,15]
        random.shuffle(remaining)
        for i in range(16):
            if rand[i] != False:
                continue
            rand[i] = tiles[remaining.pop()]
        return rand

    elif order.lower() == 'balanced':
        #generate a placeholder list to put our tile indices into
        balanced = [False,]*16
        
        
        #pick a center tile for the fountain and Caravansery which could be 5,6,9,10
        center = [5,6,9,10]
        random.shuffle(center)
        fountain = center[0]
        caravansery = center[1]
        balanced[fountain] = tiles[6]
        balanced[caravansery] = tiles[5]

        #pick a corner tile for the Tea House
        corners = [0,3,12,15]
        random.shuffle(corners)
        tea_house = corners[0]
        balanced[tea_house] = tiles[8]

        #set tiles that are at least 3 away from Tea House for Black Market and Gemstone Dealer
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
        
        #shuffle and set the Black Market and Gemstone Dealer to those tiles
        random.shuffle(dist_three)
        black_market = dist_three[0]
        gemstone_dealer = dist_three[1]
        balanced[black_market] = tiles[7]
        balanced[gemstone_dealer] = tiles[15]
        
        #set remaining tiles, shuffle them, and make sure at least 4 special are <= 2 dist from Fountain
        while True:
            test_balanced = list(balanced)
            remaining = [0,1,2,3,4,9,10,11,12,13,14]
            random.shuffle(remaining)
            special = 0
            if abs(black_market//4 - fountain//4) + abs(black_market%4 + fountain%4) <= 2:
                special += 1
            if abs(tea_house//4 - fountain//4) + abs(tea_house%4 + fountain%4) <= 2:
                special += 1
            for i in range(16):
                if test_balanced[i] != False:
                    continue
                tile = remaining.pop()
                if tile in [2,3,4,5,12] and abs(i//4 - fountain//4) + abs(i%4 - fountain%4) <= 2:
                    special += 1
                test_balanced[i] = tiles[tile]
            if special >= 4:
                return test_balanced
        
    else: 
        print("Bad input for generate_board:",order)
        return False

