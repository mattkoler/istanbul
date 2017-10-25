from sanitised_inputs import input_from_list, input_int_range
from gen_boardv2 import generate_board
from board import Board

def start_game():
    num_players = input_int_range("How many players? ", 2, 5)
    colors = ['White', 'Green', 'Red', 'Blue', 'Purple']
    p_colors = []
    for i in range(num_players):
        choice = input_from_list("What color would you like for player {}? ".format(i+1), colors)
        p_colors.append(choice)
        colors.remove(choice)
    print("You chose {} players with the colors {}.".format(num_players, str(p_colors)))
    gen_options = ['default', 'shortest', 'farthest', 'random', 'balanced']
    gen = input_from_list("How would you like to generate the board? ", gen_options)
    game_board = Board(generate_board(num_players, gen))
    game_board.print_board()

start_game()
