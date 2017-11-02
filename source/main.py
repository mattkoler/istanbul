import board, gen_boardv2, player_wagon, tile, start_game, take_turn

game_board, players = start_game.start_game()

for player in players:
    take_turn.take_turn(player, game_board)

