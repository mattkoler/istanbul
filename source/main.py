import board, gen_boardv2, player_wagon, tile

tiles = gen_boardv2.generate_board(5,'balanced')

game_board = board.Board(tiles)

game_board.print_board()