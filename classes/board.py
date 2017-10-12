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
