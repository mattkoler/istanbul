import sanitised_inputs

def take_turn(player, game_board):
    print("Here is the board:")
    game_board.print_board()
    print("It is the {} player's turn.".format(player.color))
    print("You have {} assistants in your stack.".format(player.assistants))
    print("You have {} red, {} green, {} yellow, and {} blue resources as well as {} Lira and {} gems.".format(player.red, player.green, player.yellow, player.blue, player.coins, player.gems))
    alt_action = True if player.yellow_building else False
    if alt_action and len(player.assist_locs) > 0 and sanitised_inputs.input_yes_no("Do you want to use your yellow mosque action?"):
        assist = sanitised_inputs.input_from_list("Which assistant would you like to return?",player.assist_locs)
        assist_loc = game_board.get_tile_loc(assist)
        if player.remove_lira(2) and game_board.tile[assist_loc].remove_assistant(player.color):
            player.assistants += 1
        
    #TODO: Ask for movement modifying card usage
    move_spaces = (1,2)


    while True:
        move = input("Please enter a tile to move to by name:")
        valid_move, move_loc = check_move(player.location, move, move_spaces, game_board)
        if valid_move:
            game_board.tiles[game_board.get_tile_loc(player.location)].merchants.remove(player)
            game_board.tiles[move_loc].merchants.append(player)
            player.location = move
            print("You moved to the {}.".format(move))
            break
        else:
            print("Sorry, you can't move to the {} tile.".format(move))
    
    if move == 'Fountain':
        pass
    elif player.color in game_board.tiles[move_loc].assistants:
        pickup = sanitised_inputs.input_yes_no("Would you like to pickup your assistant here? ")
        if not pickup:
            print("Your turn has ended.")
            return None
        game_board.tiles[move_loc].assistants.remove(player.color)
        player.assistants += 1
        print("You picked up your assistant.")
    elif player.assistants > 0:
        dropoff = sanitised_inputs.input_yes_no("Do you want to drop off an assistant here? ")
        if not dropoff:
            print("Your turn has ended.")
            return None
        game_board.tiles[move_loc].assistants.append(player.color)
        player.assistants -= 1
    else:
        print("Your turn ends because you can't pickup or dropoff assistants.")
        return None

    if alt_action and len(player.assist_locs) > 0 and sanitised_inputs.input_yes_no("Do you want to use your yellow mosque action?"):
        assist = sanitised_inputs.input_from_list("Which assistant would you like to return (can't be the one on this tile)?",player.assist_locs)
        assist_loc = game_board.get_tile_loc(assist) 
        if player.remove_lira(2) and game_board.tile[assist_loc].remove_assistant(player.color):
            player.assistants += 1
    
    
        
def check_move(start, move, move_spaces, game_board):
    """Takes in a starting location (name) and move location (name) of the tile
    and a range of the move spaces they can go in the form of (min,max) inclusive.
    Returns True if move is valid, otherwise False"""

    start_loc = game_board.get_tile_loc(start)
    move_loc = game_board.get_tile_loc(move)
    if not start_loc and move_loc:
        print("Something went wrong in check_move {} {}".format(start,start_loc,move,move_loc))
    
    distance = abs(start_loc//4 - move_loc//4) + abs(start_loc%4 - move_loc%4)
    print("{} tile is at location {} and {} away from your tile {} at {}".format(move,move_loc,distance,start,start_loc))
    if move_spaces[0] <= distance <= move_spaces[1]:
        return True, move_loc
    return False, -1
    
