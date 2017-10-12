# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:25:58 2017

@author: mlemons
"""

import random

class player_wagon:
    
    def __init__(self, coins):
        self.coins = coins
        self.red = self.yellow = self.green = self.blue = self.gems = 0
        self.item_max = 2
    
    def add_lira(self, lira):
        self.coins += lira
        
    def remove_lira(self, lira):
        if self.coins < lira:
            return False
        self.coins -= lira
    
    def fill_red(self):
        self.red = self.item_max
    
    def fill_yellow(self):
        self.yellow = self.item_max
        
    def fill_green(self):
        self.green = self.item_max
        
    def add_red(self):
        self.red = min(self.red+1, self.item_max)
        
    def add_yellow(self):
        self.yellow = min(self.yellow+1, self.item_max)
        
    def add_green(self):
        self.green = min(self.green+1, self.item_max)
    
    def add_blue(self):
        self.blue = min(self.blue+1, self.item_max)
        
    def add_gem(self):
        self.gems += 1
        
    def remove_red(self):
        if self.red <= 0:
            return False
        self.red -= 1
    
    def remove_yellow(self):
        if self.yellow <= 0:
            return False
        self.yellow -= 1   
    
    def remove_green(self):
        if self.green <= 0:
            return False
        self.green -= 1

    def remove_blue(self):
        if self.blue <= 0:
            return False
        self.blue -= 1
        
    def add_capacity(self):
        if self.item_max >= 5:
            return False
        self.item_max += 1

class tile:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.action = None
        self.merchants = []
        self.assistants = []
        self.family_members = []
        self.governor = False
        self.smuggler = False
        
    def get_merchants(self):
        merchs = ''
        for m in self.merchants:
            merchs += m + ' '
        return merchs
    
    def get_assistants(self):
        assist = ''
        for a in self.assistants:
            assist += a + ' '
        return assist
    
class board:
    
    #tiles should be a list of tile class objects
    def __init__(self, tiles):
        self.tiles = tiles
        self.row_1 = tiles[:4]
        self.row_2 = tiles[4:8]
        self.row_3 = tiles[8:12]
        self.row_4 = tiles[12:]
    
    def print_board(self):
        print('+-------------------+-------------------+-------------------+-------------------+')
        for row in [self.tiles[x:x+4] for x in range(0,16,4)]:
            print('| {:^18}| {:^18}| {:^18}| {:^18}|'.format(*(n.name for n in row)))
            print('| M: {0:<5} A: {4:<5} | M: {1:<5} A: {5:<5} | M: {2:<5} A: {6:<5} | M: {3:<5} A: {7:<5} |'.format(*(n.get_merchants() for n in row),*(n.get_assistants() for n in row)))
            print('| F: {} G: {} S: {} |')
            print('+-------------------+-------------------+-------------------+-------------------+')

    

#list of tiles with [name, description, action]
tiles = [
        ['Wainwright', 'Pay 7 Lira to increase you item capacity (max 3 upgrade or 5 items). Get 1 gem for getting to max.'],
        ['Fabric Warehouse', 'Fill up your wagon with the fabric (red) resource'],
        ['Spice Warehouse', 'Fill up your wagon with the spice (green) resource'],
        ['Fruit Warehouse', 'Fill up your wagon with the fruit (yellow) resource'],
        ['Post Office', 'Receive 2 resource and 2-3 Lira depending on what is uncovered'],
        ['Caravansary', 'Take 2 Bonus cards (from deck or top of discard) then discard 1'],
        ['Fountain', 'Return any number of Assistants to your Merchant stack.'],
        ['Black Market', 'Gain 1 red, yellow, or green good and roll for a chance at blue goods.'],
        ['Tea House', 'Name a number between 3-13 and match or beat it with a roll to get that amount (min 2 Lira).'],
        ['Small Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.'],
        ['Large Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.'],
        ['Police Station', 'If your family member is here, send them to do 1 action on another square.'],
        ["Sultan's Palace", 'Delivered goods in exchange for gems. Cost increases after every gem.'],
        ['Small Mosque', 'Exchange red or green goods for Mosque tiles which grant special abilities. Gather both to get a gem.'],
        ['Large Mosque', 'Exchange yellow or blue goods for Mosque tiles which grant special abilities. Gather both to get a gem.'],
        ['Gemstone Dealer', 'Pay Lira to receive gems. Cost increases after every gem.']
        ]

def probability(target):
    """Determine the probability of getting a sum >= target on a 2d6 roll where
    you may turn 1 die in a 4 OR reroll"""
    total = success = 0
    while total < 1000000:
        #check to see if first roll is high enough that a 4 on the second 
        #meets our target
        first = random.randint(1,6)
        if first >= target-4:
            success += 1
            total += 1
            continue
        #check to see if second roll is high enough that changing the
        #first roll to 4 meets out target or the sum meets the target
        second = random.randint(1,6)
        if second >= target-4 or first + second >= target:
            success += 1
            total += 1
            continue
        #failing to meet our target above, reroll (can't change to 4)
        if random.randint(1,6) + random.randint(1,6) >= target:
            success += 1
        total +=1
    return (success/total)

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


tile_list = []

for t in tiles:
    tile_list.append(tile(*t))

test_board = board(tile_list)

test_board.print_board()

tlist = ['a','b','c','d','e','f']

