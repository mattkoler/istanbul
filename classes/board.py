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
        print('| {:<18}| {:<18}| {:<18}| {:<18}|'.format(*(n.name for n in self.row_1)))
        print('| M: {:<15}| M: {:<15}| M: {:<15}| M: {:<15}|'.format(*(n.get_merchants() for n in self.row_1)))
        print('| A: {:<15}| A: {:<15}| A: {:<15}| A: {:<15}|'.format(*(n.get_assistants() for n in self.row_1)))
        print('+-------------------+-------------------+-------------------+-------------------+')
        print('| {:<18}| {:<18}| {:<18}| {:<18}|'.format(*(n.name for n in self.row_2)))
        print('| M: {:<15}| M: {:<15}| M: {:<15}| M: {:<15}|'.format(*(n.get_merchants() for n in self.row_2)))
        print('| A: {:<15}| A: {:<15}| A: {:<15}| A: {:<15}|'.format(*(n.get_assistants() for n in self.row_2)))
        print('+-------------------+-------------------+-------------------+-------------------+')
        print('| {:<18}| {:<18}| {:<18}| {:<18}|'.format(*(n.name for n in self.row_3)))
        print('| M: {:<15}| M: {:<15}| M: {:<15}| M: {:<15}|'.format(*(n.get_merchants() for n in self.row_3)))
        print('| A: {:<15}| A: {:<15}| A: {:<15}| A: {:<15}|'.format(*(n.get_assistants() for n in self.row_3)))
        print('+-------------------+-------------------+-------------------+-------------------+')
        print('| {:<18}| {:<18}| {:<18}| {:<18}|'.format(*(n.name for n in self.row_4)))
        print('| M: {:<15}| M: {:<15}| M: {:<15}| M: {:<15}|'.format(*(n.get_merchants() for n in self.row_4)))
        print('| A: {:<15}| A: {:<15}| A: {:<15}| A: {:<15}|'.format(*(n.get_assistants() for n in self.row_4)))
        print('+-------------------+-------------------+-------------------+-------------------+')
