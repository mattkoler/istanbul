from random import shuffle

class Board:
    """A Board tracks the state of the tiles and deck."""

    def __init__(self, tiles):
        """takes in a list of tiles which are all tile class objects"""
        self.tiles = tiles
        self.loc_map = {}
        for i, tile in enumerate(self.tiles):
            self.loc_map[tile.name] = i
        self.deck = ["Gain 1 resource",] * 4 + \
            ["Gain 5 Lira",] * 4 + \
            ["Carry out Sultan's Palace action an additional time",] * 2 + \
            ["Carry out Post Office action an additional time",] * 2 + \
            ["Carry out Gemstone Dealer action an additional time",] * 2 + \
            ["Return your family member to the Police Station and collect the reward",] * 2 + \
            ["Move 0 this turn instead of 1-2 (take the tile action still)",] * 2 + \
            ["Move 3-4 this turn instead of 1-2",] * 4 + \
            ["Before or immediately after movement, return 1 assistant to your stack",] * 2 + \
            ["You may sell any goods to meet the Small Market demand",] *2
        shuffle(self.deck)

    def deck_draw(self):
        """Returns a new card from the deck or False if no cards are available"""
        if len(self.deck) <= 0:
            self.deck = tile.caravansery.get_discard() #TODO: fix call to caravansery
            if len(self.deck <= 0):
                return False
            shuffle(self.deck)
        return self.deck.pop()

    def print_board(self):
        """Prints board in command line format"""
        print('+-------------------+-------------------+-------------------+-------------------+')
        for row in [self.tiles[x:x+4] for x in range(0, 16, 4)]:
            print('|{}|{}|{}|{}|'.format(*(n.get_first_row() for n in row)))
            print('|{}|{}|{}|{}|'.format(*(n.get_second_row() for n in row)))
            print('|{}|{}|{}|{}|'.format(*(n.get_third_row() for n in row)))
            print('+-------------------+-------------------+-------------------+-------------------+')

    def get_tile_loc(self, name):
        """Takes in name as a string and returns the location of the tile, if name is invalid returns False"""
        if name in self.loc_map:
            return self.loc_map[name]
        return False

    def get_tile_name(self, loc):
        """Takes in loc as an int and returns the name of the tile, if loc is invalid returns False"""
        for key, value in self.loc_map.items():
            if value == loc:
                return key
        return False
