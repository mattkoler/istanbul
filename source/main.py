import board, gen_boardv2, player_wagon, tile, start_game, take_turn, copy

game_board, players = start_game.start_game()

for player in players:
    take_turn.take_turn(player, players game_board)

game_board.print_board()