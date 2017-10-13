def take_turn(player):
    """Takes in a player object of class PlayerWagon and steps them through taking their turn
    Turns have the following sequence:
        1. Movement
            a. If player has the yellow Mosque tile, they may pay 2 Lira to gain and assistant
            b. A player may play a bonus card
            c. Carry out movement for the turn
            d. Either pick up an assistant or drop one off
                -A player may choose to do neither and their turn immediately ends unless on Fountain
        2. Encounters with other Merchants (if any)
            a. A player may play a bonus card
            b. If the tile is not the Fountain, pay 2 Lira to any other merchants on the tile
                -If unable, turn ends immediately
            c. In a 2 player game, roll to move the neutral merchants to a new tile
        3. Tile Action
            a. A player may play a bonus card
            b. A player may carry out the action on the tile
        4. Encounters in any order
            a. Family member - must send them back (except your own) and gain 3 Lira or 1 bonus card
            b. May use Governor to draw 1 bonus card and discard 1 or pay 2 Lira to keep it
                -If used, roll to move them
            c. May use Smuggler to gain 1 resource of choice then lose 1 resource or spend 2 Lira
                -If used, roll to move them
    """
