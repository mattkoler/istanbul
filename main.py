from classes.board import Board
from classes.tile import Tile
from classes.player_wagon import PlayerWagon
from functions.generate_board import generate_board

#list of tiles with [name, description, action]
tiles = [
        ['Wainwright', 'Pay 7 Lira to increase you item capacity (max 3 upgrade or 5 items). Get 1 gem for getting to max.'],
        ['Fabric Warehouse', 'Fill up your wagon with the fabric (red) resource'],
        ['Spice Warehouse', 'Fill up your wagon with the spice (green) resource'],
        ['Fruit Warehouse', 'Fill up your wagon with the fruit (yellow) resource'],
        ['Post Office', 'Receive 2 resource and 2-3 Lira depending on what is uncovered'],
        ['Caravansary', 'Take 2 Bonus cards (from deck or top of discard) then discard 1'],
        ['Fountain', 'Return any number of Assistants to your Merchant stack.'],
        ['Black Market', 'Gain 1 red, yellow, or green good and roll for a chance at blue goods.'],
        ['Tea House', 'Name a number between 3-13 and match or beat it with a roll to get that amount (min 2 Lira).'],
        ['Small Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.'],
        ['Large Market', 'Sell 1-5 goods depicted on the demand square for Lira, then rotate demand.'],
        ['Police Station', 'If your family member is here, send them to do 1 action on another square.'],
        ["Sultan's Palace", 'Delivered goods in exchange for gems. Cost increases after every gem.'],
        ['Small Mosque', 'Exchange red or green goods for Mosque tiles which grant special abilities. Gather both to get a gem.'],
        ['Large Mosque', 'Exchange yellow or blue goods for Mosque tiles which grant special abilities. Gather both to get a gem.'],
        ['Gemstone Dealer', 'Pay Lira to receive gems. Cost increases after every gem.']
        ]


tile_list = []

for t in tiles:
        tile_list.append(Tile(*t))


generate_board()