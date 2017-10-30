from sanitised_inputs import input_from_list, input_int_range
from gen_boardv2 import generate_board
from board import Board
from player_wagon import PlayerWagon
from convert_tile import tile_num_to_name
from random import randint

def start_game():
    """Asks how many players, what colors, and board generation
    Then instantiates a board, TODO: a player object for each color,
        determines turn order, and TODO: gives out Lira for turn position
    Returns a board object and turn order
    """

    #asks for number of players
    num_players = input_int_range("How many players? ", 2, 5)

    #asks for colors and puts them into a list
    colors = ['white', 'green', 'red', 'blue', 'purple']
    p_colors = []
    for i in range(num_players):
        choice = input_from_list("What color would you like for player {}? ".format(i+1), colors)
        p_colors.append(choice)
        colors.remove(choice)
    print("You chose {} players with the colors: {}.".format(num_players, ", ".join(p_colors)))

    #randomly determine starting player then create player objects for each color
    starting_player = randint(1,num_players)
    p_colors = p_colors[starting_player-1:] + p_colors[:starting_player-1]
    p_objects = []
    for i,p_col in enumerate(p_colors):
        p_objects.append(PlayerWagon(p_col[:1],i+1))

    #ask how the board should be generated
    gen_options = ['default', 'shortest', 'farthest', 'random', 'balanced']
    gen = input_from_list("How would you like to generate the board? ", gen_options)
    game_board = Board(generate_board(num_players, gen))

    #put all players at the fountain tile and set governor and smuggler
    gov = tile_num_to_name(randint(1,6) + randint(1,6))
    smug = tile_num_to_name(randint(1,6) + randint(1,6))
    print(gov,smug)
    for tile in game_board.tiles:
        if tile.name == "Fountain":
            tile.merchants = p_objects
        if tile.name == gov:
            tile.governor = True
        if tile.name == smug:
            tile.smuggler = True
    print("Here is your board:")
    game_board.print_board()
    


start_game()
