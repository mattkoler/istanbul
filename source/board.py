from random import shuffle

class Board:
    
    def __init__(self, tiles):
        """takes in a list of tiles which are all tile class objects"""
        self.tiles = tiles
        self.deck = ["Gain 1 resource",] * 4 + \
            ["Gain 5 Lira",] * 4 + \
            ["Carry out Sultan's Palace action an additional time",] * 2 + \
            ["Carry out Post Office action an additional time",] * 2 + \
            ["Carry out Gemstone Dealer action an additional time",] * 2 + \
            ["Return your family member to the Police Station and collect the reward",] * 2 + \
            ["Move 0 this turn instead of 1-2 (take the tile action still)",] * 2 + \
            ["Move 3-4 this turn instead of 1-2",] * 4 + \
            ["Before or immediately after movement, return 1 assistant to your stack",] * 2 + \
            ["You may sell any goods to meet the Small Market demand"] *2
        shuffle(self.deck)

    def deck_draw(self):
        if len(self.deck) <= 0:
            self.deck = tile.caravansery.get_discard() #TODO: fix call to caravansery
            if len(self.deck <= 0):
                return False
            shuffle(self.deck)
        return self.deck.pop()

    def print_board(self):
        print('+-------------------+-------------------+-------------------+-------------------+')
        for row in [self.tiles[x:x+4] for x in range(0,16,4)]:
            print('| {:^18}| {:^18}| {:^18}| {:^18}|'.format(*(n.name for n in row)))
            #print('| M: {0:<5} A: {4:<5} | M: {1:<5} A: {5:<5} | M: {2:<5} A: {6:<5} | M: {3:<5} A: {7:<5} |'.format(*(n.get_merchants() for n in row),*(n.get_assistants() for n in row)))
            #print('| F: {} G: {} S: {} |')
            print('+-------------------+-------------------+-------------------+-------------------+')
