import sanitised_inputs

def take_turn(player, players, game_board):
    print("Here is the board:")
    game_board.print_board()
    print("It is the {} player's turn.".format(player.color))
    print("You have {} assistants in your stack.".format(player.assistants))
    print("You have {} red, {} green, {} yellow, and {} blue resources as well as {} Lira and {} gems.".format(player.red, player.green, player.yellow, player.blue, player.coins, player.gems))

    #Start Phase 1 - Movement

    #check to see if player has the yellow building, assistants not in their stack, and wants to take that action
    alt_action = True if player.yellow_building else False
    if alt_action and len(player.assist_locs) > 0 and sanitised_inputs.input_yes_no("Do you want to use your yellow mosque action?"):
        assist = sanitised_inputs.input_from_list("Which assistant would you like to return?",player.assist_locs) #TODO: make sure player isn't picking up assistant from the same tile they are on
        assist_loc = game_board.get_tile_loc(assist)
        if player.remove_lira(2) and game_board.tile[assist_loc].remove_assistant(player.color):
            player.assistants += 1
        
    #TODO: Ask for movement modifying card usage
    move_spaces = (1,2)

    #Ask where the player wants to move and verify it is a legal move, then update the tiles and player location
    while True:
        move = input("Please enter a tile to move to by name:")
        valid_move, move_loc = check_move(player.location, move, move_spaces, game_board)
        if valid_move:
            game_board.tiles[game_board.get_tile_loc(player.location)].remove_merchant(player.color)
            game_board.tiles[move_loc].merchants.append(player.color)
            player.location = move
            print("You moved to the {}.".format(move))
            break
        else:
            print("Sorry, you can't move to the {} tile.".format(move))
    
    #If player ended up on the Fountain, assistant actions can be carried out with the Fountain's tile action
    if move == 'Fountain':
        pass
    #If the player moves to a tile that has one of their assistants, they need to pick it up or end their turn
    elif player.color in game_board.tiles[move_loc].assistants:
        pickup = sanitised_inputs.input_yes_no("Would you like to pickup your assistant here? ")
        if not pickup:
            print("Your turn has ended.")
            return None
        game_board.tiles[move_loc].assistants.remove(player.color)
        player.assistants += 1
        print("You picked up your assistant.")
    #If a player moves to a tile without one of their assistants, they need to drop it of for end their turn
    elif player.assistants > 0:
        dropoff = sanitised_inputs.input_yes_no("Do you want to drop off an assistant here? ")
        if not dropoff:
            print("Your turn has ended.")
            return None
        game_board.tiles[move_loc].assistants.append(player.color)
        player.assistants -= 1
    #If a player moves to a tile without any assistants nor has any, they end their turn
    else:
        print("Your turn ends because you can't pickup or dropoff assistants.")
        return None

    #After movement, ask the player if they want to use their yellow building action if they didn't earlier in the phase
    if alt_action and len(player.assist_locs) > 0 and sanitised_inputs.input_yes_no("Do you want to use your yellow mosque action?"):
        assist = sanitised_inputs.input_from_list("Which assistant would you like to return (can't be the one on this tile)?",player.assist_locs)
        assist_loc = game_board.get_tile_loc(assist) 
        if player.remove_lira(2) and game_board.tile[assist_loc].remove_assistant(player.color):
            player.assistants += 1
    
    #End Phase 1 - Movement
    
    #Start Phase 2 - Encounters with other Merchants
    other_merchants = []
    for merch in game_board.tiles[move_loc].merchants:
        if merch == player.color:
            continue
        other_merchants.append(merch)
    
    #Check to see if there are other merchants on the square and they aren't on the Fountain where it doesn't matter
    if len(other_merchants) > 0 and move != "Fountain":
        print("You must pay these other merchants 2 Lira each or end your turn: {}".format(other_merchants))
        #player can't afford to pay other merchants
        if player.get_coins() < len(other_merchants) * 2:
            print("You don't have enough Lira to pay the other merchants here 2 each. End turn")
            return None
        #ask them if they want to pay, end turn if no otherwise move Lira around
        pay = sanitised_inputs.input_yes_no("Do you want to pay a total of {} Lira to them?")
        if not pay:
            print("You chose not to pay so your turn in ended")
            return None
        for merchant in other_merchants:
            for p in players:
                if p.color == merchant:
                    p.add_lira(2)
        player.remove_lira(len(other_merchants)*2)
        print("You paid a total of {} Lira to the other merchants".format(len(other_merchants)*2))
    #TODO: Implement 2 player nuetral merchants rerolls
    #End Phase 2 - Movement

    #Start Phase 3 - Action (tile)
    #End Phase 3 - Action (tile)

    #Start Phase 4 - Encounters
    #End Phase 4 - Encounters
        
def check_move(start, move, move_spaces, game_board):
    """Takes in a starting location (name) and move location (name) of the tile
    and a range of the move spaces they can go in the form of (min,max) inclusive.
    Returns True if move is valid, otherwise False"""

    start_loc = game_board.get_tile_loc(start)
    move_loc = game_board.get_tile_loc(move)
    if not start_loc and move_loc:
        print("Something went wrong in check_move {} {}".format(start,move,))
    
    distance = abs(start_loc//4 - move_loc//4) + abs(start_loc%4 - move_loc%4)
    print("{} tile is at location {} and {} away from your tile {} at {}".format(move,move_loc,distance,start,start_loc))
    if move_spaces[0] <= distance <= move_spaces[1]:
        return True, move_loc
    return False, -1
    
