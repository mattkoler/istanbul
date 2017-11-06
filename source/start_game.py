from sanitised_inputs import input_from_list, input_int_range
from gen_boardv2 import generate_board
from board import Board
from player_wagon import PlayerWagon
from convert_tile import tile_num_to_name
from random import randint

def start_game():
    """
    Asks how many players, what colors, and board generation
    Then instantiates a board, a player object for each color,
    determines turn order, and gives out Lira for turn position
    Returns a board object and turn order
    """

    # asks for number of players
    num_players = input_int_range("How many players? ", 2, 5)

    # asks for player colors then creates the player object of that color
    colors = ['white', 'green', 'red', 'blue', 'purple']
    p_objects = []
    for i in range(1, num_players+1):
        choice = input_from_list("What color would you like for player {}? ".format(i), colors)
        p_objects.append(PlayerWagon(choice, i))
        colors.remove(choice)

    # randomly determine starting player
    starting_player = randint(1, num_players)
    p_objects = p_objects[starting_player-1:] + p_objects[:starting_player-1]
    print("The turn order will be: {}".format([p.color for p in p_objects]))

    # ask how the board should be generated
    gen_options = ['default', 'shortest', 'farthest', 'random', 'balanced']
    gen = input_from_list("How would you like to generate the board? ", gen_options)
    game_board = Board(generate_board(num_players, gen))


    # put all players at the fountain tile and set governor and smuggler
    gov = tile_num_to_name(randint(1, 6) + randint(1, 6)) # TODO: Replace randint with roll module
    smug = tile_num_to_name(randint(1, 6) + randint(1, 6))
    for tile in game_board.tiles:
        if tile.name == "Fountain":
            for p in p_objects:
                tile.merchants.append(p.color)
        if tile.name == gov:
            tile.governor = True
        if tile.name == smug:
            tile.smuggler = True

    return (game_board, p_objects)
