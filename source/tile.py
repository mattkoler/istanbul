#list of tiles with [name, description, id]
tiles = [
        ['Wainwright', 'Pay 7 Lira to increase you item capacity (max 3 upgrade or 5 items). Get 1 gem for getting to max.', 1],
        ['Fabric Warehouse', 'Fill up your wagon with the fabric (red) resource', 2],
        ['Spice Warehouse', 'Fill up your wagon with the spice (green) resource', 3],
        ['Fruit Warehouse', 'Fill up your wagon with the fruit (yellow) resource', 4],
        ['Post Office', 'Receive 2 resource and 2-3 Lira depending on what is uncovered', 5],
        ['Caravansary', 'Take 2 Bonus cards (from deck or top of discard) then discard 1', 6],
        ['Fountain', 'Return any number of Assistants to your Merchant stack.', 7],
        ['Black Market', 'Gain 1 red, yellow, or green good and roll for a chance at blue goods.', 8],
        ['Tea House', 'Name a number between 3-13 and match or beat it with a roll to get that amount (min 2 Lira).', 9],
        ['Small Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.', 10],
        ['Large Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.', 11],
        ['Police Station', 'If your family member is here, send them to do 1 action on another square.', 12],
        ["Sultan's Palace", 'Delivered goods in exchange for gems. Cost increases after every gem.', 13],
        ['Small Mosque', 'Exchange red or green goods for Mosque tiles which grant special abilities. Gather both to get a gem.', 14],
        ['Large Mosque', 'Exchange yellow or blue goods for Mosque tiles which grant special abilities. Gather both to get a gem.', 15],
        ['Gemstone Dealer', 'Pay Lira to receive gems. Cost increases after every gem.', 16]
        ]

class Tile:
    
    def __init__(self):
        self.merchants = []
        self.assistants = []
        self.family = []
        self.governor = self.smuggler = False
        
    def get_merchants(self):
        merchs = ''
        for m in self.merchants:
            merchs += m.color[0]
        return merchs

    def get_assistants(self):
        assistants = ''
        for assist in self.assistants:
            assistants += assist[0]
        return assistants

    def get_family(self):
        family = ''
        for fam in self.family:
            family += fam + ' '
        return family

    def get_first_row(self):
        '''returns name centered in 18 char str'''
        return ' {:^18}'.format(self.name)

    def get_second_row(self):
        '''returns mercs and assistants in 18 char str'''
        return ' M:{:<7} A:{:<6}'.format(self.get_merchants(), self.get_assistants())

    def get_third_row(self):
        '''returns family, smuggler, and governor in 18 char str'''
        return ' F: {:<5} {:>4} {:<4}'.format(self.get_family(), 'G' if self.governor else '', 'S' if self.smuggler else '')

    def remove_assistant(self, player_color):
        if player_color in self.assistants:
            self.assistant.remove(player_color)
            return True
        return False

class Wainwright(Tile):
    """Special class for the Wainwright tile. Takes in players as a list of player colors
    e.g. [R,G,Y] for 3 players of colors Red, Green, and Yellow"""
    def __init__(self, num_players):
        super().__init__()
        self.num_players = self.gems = num_players
        self.name = "Wainwright"
        self.sp_resource = ['Wagon Pieces', 3*num_players]

    def tile_action(self, player):
        """
        check to see if player has room to upgrade
        check to see if player has 7 lira
        take lira, give upgrade, remove 1 wagon piece
        check to see if player has max upgrades, give gem if so and remove gem """
        if player.item_max() >= 5:
            print("Sorry, you can't upgrade your wagon anymore")
            return None
        if player.remove_lira(7):
            player.add_capacity()
            print("You have upgraded your wagon and can hold {} of each resource now.".format(player.item_max()))
            if player.item_max() == 5:
                print("You have gotten all 3 upgrades and gained a gem")
                player.add_gem()
                self.gems -= 1

class FabricWarehouse(Tile):
    """Special class for the Fabric Warehouse tile. Gives a player max Fabric (red) resource"""
    def __init__(self):
        super().__init__()
        self.name = "Fabric Warehouse"

    def tile_action(self, player):
        player.fill_red()

class SpiceWarehouse(Tile):
    """Special class for the Spice Warehouse tile. Gives a player max Spice (green) resource"""
    def __init__(self):
        super().__init__()
        self.name = "Spice Warehouse"

    def tile_action(self, player):
        player.fill_green()

class FruitWarehouse(Tile):
    """Special class for the Fruit Warehouse tile. Gives a player max Fruit (yellow) resource"""
    def __init__(self):
        super().__init__()
        self.name = "Fruit Warehouse"

    def tile_action(self, player):
        player.fill_yellow()

class PostOffice(Tile):
    """Special class for the Post Office tile. Gives a rotating set of Goods and Lira"""

    def __init__(self):
        super().__init__()
        self.name = "Post Office"
        self.goods = (
            (2, 'G', 'Y'),
            (2, 'R', 'Y'),
            (3, 'R', 'Y'),
            (3, 'R', 'B'),
            (4, 'R', 'B')
        )
        self.current = 0

    def tile_action(self, player):
        for item in self.goods[current]:
            if type(item) == 'int':
                player.add_lira(item)
            elif item == 'G':
                player.add_green()
            elif item == 'Y':
                player.add_yellow()
            elif item == 'R':
                player.add_red()
            elif item == 'B':
                player.add_blue()
        self.current += 1
        if self.current >= 5:
            self.current = 0
    

class Caravansary(Tile):
    """Special class for the Caravansary tile. Allows player to draw 2 cards from either deck
    or the top of the discard pile, then discard 1 from their hand"""
    def __init__(self):
        super().__init__()
        self.discard = []
        self.name = "Caravansary"
    
    def tile_action(self, player):
        cards_drawn = 0
        while cards_drawn < 2:
            if len(self.discard) == 0:
                card_draw = board.deck_draw()
                if not card_draw:
                    print('Sorry, there are no cards in deck or discard')
                    return None
                print('You draw a card from the deck (no discard available).')
                player.add_card(card_draw)
            else:
                choice = ''
                while choice.lower() not in ('deck', 'discard'):
                    choice = input('Would you like to draw from the deck or discard?')
                if choice.lower() == 'deck':
                    print('You draw a card from the deck')
                    player.add_card(board.deck_draw())
                else:
                    print('You draw the top card of the discard pile')
                    player.add_card(self.discard.pop(0))
            cards_drawn += 1
    pass

class Fountain(Tile):
    """Special class for the Fountain tile. When a player lands here, they may return any amount
    of their assistants to their stack. They also do not pay other merchants on this space."""
    def __init__(self):
        super().__init__()
        self.name = "Fountain"

    #ask player which assistants they would like to return
    def tile_action(self, player):
        for loc in player.assist_locs:
            while True:
                ans = input("Would you like to return your assistant at {} to your stack? y/n".format(loc))
                if ans.lower() == 'y':
                    player.assist_locs.remove(loc)
                    player.assistants += 1
                    break
                elif ans.lower() == 'n':
                    break
                print("Sorry, I didn't quite catch that.")
    

class BlackMarket(Tile):
    """Special class for the Black Market tile. Allows a player to pick 1 of R/Y/G resource and
    roll dice to try to get blue"""
    #prompt player which R/Y/G they want
    #roll 2d6 for blue (7-8 = 1, 9-10 = 2, 11-12 = 3)
    #make sure to check for special ability
    def __init__(self):
        super().__init__()
        self.name = "Black Market"

    def tile_action(self, player):
        while True:
            ans = input("What resource would you like 1 of? r/y/g")
            if ans.lower() == 'r':
                player.add_red()
                break
            elif ans.lower() == 'y':
                player.add_yellow()
                break
            elif ans.lower() == 'g':
                player.add_green
                break
            print("Sorry I didn't catch that.")
        if player.red_building:
            roll = (random.randint(1,6),random.randint(1,6))
            print("You rolled a {} and a {} for a total of {}.".format(roll[0],roll[1],sum(roll)))
            while True:
                ans = input("You may (c)hange the {} into a 4, (r)eroll, or (a)ccept the roll: ".format(min(roll)))
                if ans.lower() == 'c':
                    roll = (max(roll),4)
                    break
                elif ans.lower() == 'r':
                    roll = (random.randint(1,6),random.randint(1,6))
                    break
                elif ans.lower() == 'a':
                    break
                print("Sorry I didn't catch that.")
        else:
            roll = (random.randint(1,6),random.randint(1,6))
            print("You rolled a {} and a {} for a total of {}.".format(roll[0],roll[1],sum(roll)))
        total = sum(roll)
        if total > 6:
            player.add_blue()
        if total > 8:
            player.add_blue()
        if total > 10:
            player.add_blue()

            
class TeaHouse(Tile):
    """Special class for the Tea House tile. Allows the player to name a number then roll dice
    to get the named number in Lira if the dice are >=. If fail, player gets 2 Lira"""
    def __init__(self):
        super().__init__()
        self.name = "Tea House"

    #prompt player to choose a number between 3-12
    #roll dice
    #pay number or 2 Lira

    def tile_action(self, player):
        target = input("Please choose a number: ")
        if player.red_building:
            roll = (random.randint(1,6),random.randint(1,6))
            print("You rolled a {} and a {} for a total of {}.".format(roll[0],roll[1],sum(roll)))
            while True:
                ans = input("You may (c)hange the {} into a 4, (r)eroll, or (a)ccept the roll: ".format(min(roll)))
                if ans.lower() == 'c':
                    roll = (max(roll),4)
                    break
                elif ans.lower() == 'r':
                    roll = (random.randint(1,6),random.randint(1,6))
                    break
                elif ans.lower() == 'a':
                    break
                print("Sorry I didn't catch that.")
        else:
            roll = (random.randint(1,6),random.randint(1,6))
            print("You rolled a {} and a {} for a total of {}.".format(roll[0],roll[1],sum(roll)))
        total = sum(roll)
        if total >= target:
            player.add_lira(target)
            print("Congrats, you rolled a total of {} and got your {} Lira.".format(total,target))
        else:
            player.add_lira(2)
            print("Sorry, you only rolled a total of {} which is below your target of {}. You still gain 2 Lira.".format(total,target))

class SmallMarket(Tile):
    """Special class for the Small Market tile. Allows players to sell resources for Lira depending
    on the amount of resources sold. The resource demand rotates through several tiles.
    Payouts for 1/2/3/4/5 resources are 2/5/9/14/20"""
    def __init__(self):
        super().__init__()
        self.name = "Small Market"
        self.demands = (
            ('b','r','g','y','y'),
            #TODO: add other tiles
        )
        self.current = 0
        self.lira= (2,5,9,14,20)

    def tile_action(self, player):
        print("The market is currently buying {} resources.".format(self.demand[self.curren]))
        while True:
            ans = input("What would you like to sell? (ex. rrb for 2 reds and a blue): ")
            test_demand = list(self.demands[self.current])
            bad_ans = False
            for c in ans:
                try:
                    test_demand.remove(c)
                except ValueError:
                    print("Sorry you can't sell this combination: {}".format(ans))
                    bad_ans = True
                    break
            if bad_ans:
                continue
            if not player.check_resources(list(ans)):
                print("Sorry you don't have those resources to sell")
                continue
            break
        #TODO: remove resources
        player.add_lira(self.lira[len(ans)])
        self.current += 1
        if self.current >= 5:
            self.current = 0

        


class LargeMarket(Tile):
    """Special class for the Large Market tile. Allows players to sell resources for Lira depending
    on the amount of resources sold. The resource demand rotates through several tiles.
    Payouts for 1/2/3/4/5 resources are 3/7/12/18/25"""

    def __init__(self):
        super().__init__()
        self.name = "Large Market"
        self.demands = (
            ('R','B','B','G','Y'),
            #TODO: add other tiles
        )
        self.currnet = 0

    #look at current demand and ask player what they want to sell
    #check to make sure player has required resources
    #remove resources and give Lira
    #rotate demand
    pass

class PoliceStation(Tile):
    """Special class for the Police Station tile. Allows players to send their family member to
    any other tile and take the action there ignoring any other merchants."""

    def __init__(self):
        super().__init__()
        self.name = "Police Station"
    #set all family members here on start

    #check that the player has a family member here, otherwise pass
    #remove the family member and put them on another tile
    #execute the tile action of that tile
    pass

class SultansPalace(Tile):
    """Special class for the Sultan's Palace tile. Allows players to trade goods for gems with
    each subsequent gem requiring more goods"""

    def __init__(self, num_players):
        super().__init__()
        self.name = "Sultan's Palace"
        self.players = num_players
        self.cost = ('B','R','G','Y','A','B','R','G','Y','A')
        self.current = 4 if num_players > 3 else 5

    def tile_action(self, player):
        current_cost = self.cost[:self.current]
        #query player to see if they have the resources
        #ask player what resources to spend for the any
        #deduct resources and give gem
        #increment current (note: if current >9 then there are no gems)
    
    pass

class SmallMosque(Tile):
    """Special class for the Small Mosque tile. Allows players to exchange resources (red or green) for
    buildings that grants special abilities. Cost increases after every purchase of a particular tile.
    Red - reroll dice or change 1 die to a 4 at Tea House or Black Market
    Green - When at a warehouse, may pay 2 Lira for 1 of any resource
    """

    def __init__(self, num_players):
        super().__init__()
        self.name = "Small Mosque"
        self.cost = (2,4) if num_players == 2 else (2,3,4,5)
        self.gems = min(num_players, 4)
        self.red_cost = self.green_cost = 0

    def tile_action(self, player):
        #ask player which tile (red/green) they would like to purchase
        #get tile cost and check that player can pay for it
        #deduct resources, flag the player for that building, increase cost
        #if players has both buildings, give a gem if there is still one
        pass
    pass

class GreatMosque(Tile):
    """Special class for the Small Mosque tile. Allows players to exchange resources (yellow or blue) for
    buildings that grants special abilities. Cost increases after every purchase of a particular tile.
    Yellow - May pay 2 Lira to retrieve and assistant from anywhere
    Blue - Get an extra assistant
    """

    def __init__(self, num_players):
        super().__init__()
        self.name = "Great Mosque"
        self.cost = (2,4) if num_players == 2 else (2,3,4,5)
        self.gems = min(num_players, 4)
        self.yellow_cost = self.blue_cost = 0

    def tile_action(self, player):
        #ask player which tile (yellow/blue) they would like to purchase
        #get tile cost and check that player can pay for it
        #deduct resources, flag the player for that building, increase cost
        #if players has both buildings, give a gem if there is still one
        pass
    pass

class GemstoneDealer(Tile):
    """Special class for Gemstone Dealer tile. Allows players to purchase gems for increasing cost"""

    def __init__(self, num_players):
        super().__init__()
        self.name = "Gemstone Dealer"
        self.cost = (12,13,14,15,16,17,18,19,20,21,22,23)
        if num_players >= 4:
            self.current = 0 
        elif num_players == 3:
            self.current = 2
        else:
            self.current = 3

    def tile_action(self, players):
        current_cost = self.cost[self.current]
        if player.remove_lira(current_cost):
            player.add_gem()
            self.current += 1