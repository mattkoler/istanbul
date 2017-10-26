from lxml import html
import requests
from difflib import SequenceMatcher
from operator import itemgetter
import heapq
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

"""
for i in range(1,92,10):
    page = requests.get('http://www.dicetower.com/game-video/zee-garcias-top-100-games-all-time-2017-{}-{}'.format(i+9,i))
    tree = html.fromstring(page.content)
    titles = tree.find_class('gt_title')


    for title in titles[::-1]:
        print(title.text_content())
"""

tom = [
    "Gloomhaven",
    "Cosmic Encounter",
    "Le Havre",
    "Summoner Wars",
    "Kemet",
    "Heroscape",
    "Arcadia Quest",
    "Caverna: The Cave Farmers",
    "Dice Masters",
    "Viticulture",
    "Thunderstone Quest",
    "Project: Elite",
    "Legendary: Marvel",
    "Champions of Midgard",
    "Race for the Galaxy",
    "Rising Sun",
    "Ticket to Ride",
    "Terraforming Mars",
    "Blood Rage",
    "Pitchcar",
    "Codex: Card-Time Strategy",
    "Time's Up!",
    "Glenn Drover's Empires: Age of Discovery – Deluxe Edition",
    "Dominion",
    "Ghost Stories",
    "Eldritch Horror",
    "Mansions of Madness: Second Edition",
    "Duel of Ages II",
    "Roll for the Galaxy",
    "Descent: Journeys in the Dark (Second Edition)",
    "Near and Far",
    "Teenage Mutant Ninja Turtles: Shadows of the Past",
    "Cyclades",
    "Balderdash",
    "BattleLore (Second Edition)",
    "Sheriff of Nottingham",
    "T.I.M.E Stories: The Marcy Case",
    "Adventure Land",
    "Catacombs",
    "Orléans",
    "Puerto Rico",
    "Clank!",
    "VIRAL",
    "Cry Havoc",
    "El Grande",
    "Twilight Struggle",
    "Automania",
    "Lords of Waterdeep",
    "Mage Wars Academy",
    "Airlines Europe",
    "Suburbia",
    "Stockpile",
    "Flick 'em Up!",
    "Captain Sonar",
    "The Voyages of Marco Polo",
    "Concept",
    "Carson City",
    "Battleground: Fantasy Warfare",
    "Mechs vs Minions",
    "Century: Spice Road",
    "Rum and Bones: Second Tide",
    "Photosynthesis",
    "Santorini",
    "Spyfall",
    "Dixit",
    "Defenders of the Last Stand",
    "Tiefe Taschen",
    "Magic Maze",
    "Francis Drake",
    "Wallenstein (second edition)",
    "Colosseum",
    "The Godfather: The Board Game",
    "Commands & Colors: Ancients",
    "Tumblin-Dice",
    "Seasons",
    "Dream Factory",
    "Libertalia",
    "Domaine",
    "Onitama",
    "Werewolf",
    "Battle Line",
    "Memoir '44",
    "Thunder & Lightning",
    "Downforce",
    "Through the Ages: A New Story of Civilization",
    "Robinson Crusoe: Adventure on the Cursed Island",
    "Star Wars: Armada",
    "A Feast for Odin",
    "Dungeon Twister",
    "When I Dream",
    "Targi",
    "Yokohama",
    "King of Tokyo",
    "Star Wars: Rebellion",
    "Pandemic Legacy",
    "Smash Up",
    "Zendo",
    "Innovation",
    "Werewords",
    "The Chameleon",
    ]

eric = [
    "Merchant of Venus",
    "Pandemic",
    "Alien Frontiers",
    "Power Grid",
    "Mice and Mystics",
    "Dominion",
    "Viticulture",
    "Mechs vs Minions",
    "Through the Ages: A New Story of Civilization",
    "Pandemic Legacy",
    "Potion Explosion",
    "Tiny Epic Galaxies",
    "Unlock!",
    "Pandemic: The Cure",
    "Istanbul",
    "Legendary Encounters: An Alien Deck Building Game",
    "T.I.M.E Stories: The Marcy Case",
    "Splendor",
    "RoboRally",
    "Antike",
    "Agricola",
    "Food Chain Magnate",
    "Scythe",
    "Pathfinder Adventure Card Game: Rise of the Runelords – Base Set",
    "Roll for the Galaxy",
    "Indonesia",
    "Legendary: A Marvel Deck Building Game",
    "King of Tokyo",
    "Logistico",
    "Xia: Legends of a Drift System",
    "Race for the Galaxy",
    "Flip City",
    "Paperback",
    "Codenames",
    "Orléans",
    "Great Western Trail",
    "Concordia",
    "Eclipse",
    "Terra Mystica",
    "Firefly: The Game",
    "TransAmerica",
    "Specter Ops",
    "Flash Point: Fire Rescue",
    "Attika",
    "Fantastiqa",
    "Bus",
    "Machi Koro",
    "Innovation",
    "Perry Rhodan: The Cosmic League",
    "Mysterium",
    "The Networks",
    "Terraforming Mars",
    "Merchant of Venus (second edition)",
    "Valley of the Kings",
    "Harry Potter Hogwarts Battle Cooperative Deck-Building Game",
    "Ticket to Ride",
    "Blood Rage",
    "Spyfall",
    "Airlines Europe",
    "Imperial",
    "Guildhall",
    "Quicksilver",
    "Trains",
    "Myrmes",
    "VOLT: Robot Battle Arena",
    "Police Precinct",
    "Adrenaline",
    "EXIT: The Game – The Pharaoh's Tomb",
    "Mage Knight Board Game",
    "Sentinels of the Multiverse",
    "KLASK",
    "Snow Tails",
    "Dice City",
    "Clank!",
    "Empires of the Void",
    "Thunderstone",
    "Impulse",
    "Die Magier von Pangea",
    "Reef Encounter",
    "Copycat",
    "Castles of Mad King Ludwig",
    "Defenders of the Realm",
    "Power Grid: The Card Game",
    "Century: Spice Road",
    "Tragedy Looper",
    "Pueblo",
    "Robinson Crusoe: Adventure on the Cursed Island",
    "Panamax",
    "Hero Realms",
    "Glass Road",
    "Eminent Domain",
    "Auf Achse",
    "Puzzle Strike",
    "Entdecker",
    "No Thanks!",
    "Escape: The Curse of the Temple",
    "Risk Legacy",
    "Red7",
    "Star Trek: Fleet Captains",
    "Space Cadets: Dice Duel",
]

sam = [
    "Blood Rage",
    "TI4",
    "Memoir '44",
    "Star Wars Rebellion",
    "Zombicide: Black Plague",
    "Deception: Murder in Hong Kong",
    "Rum and Bones: Second Tide",
    "Conan",
    "Sword & Sorcery",
    "Tournament at Camelot",
    "TZAAR",
    "Imperial Settlers",
    "Asante",
    "YINSH",
    "Five Tribes",
    "Sentient",
    "51st State Master Set",
    "Balderdash",
    "Race for the Galaxy",
    "Targi",
    "Onitama",
    "Bang! The Dice Game",
    "Stone Age",
    "V-Commandos",
    "Rising 5: Runes of Asteros",
    "Wasteland Express Delivery Service",
    "Kingsburg (Second Edition)",
    "Dead of Winter: A Crossroads Game",
    "Mission: Red Planet",
    "Hero Realms",
    "King of Tokyo",
    "Tannhäuser",
    "Star Wars: Imperial Assault",
    "Summoner Wars",
    "Sheriff of Nottingham",
    "Inis",
    "Codinca",
    "Run, Fight, or Die!",
    "Dice Town",
    "Thunderstone Advance: Numenera",
    "Bunny Kingdom",
    "Spoils of War",
    "Wettlauf nach El Dorado",
    "Sola Fide: The Reformation",
    "Photosynthesis",
    "Age of War",
    "VIRAL",
    "Specter Ops",
    "Cutthroat Kingdoms",
    "Cry Havoc",
    "Commissioned",
    "Cosmic Encounter",
    "Flick 'em Up!: Dead of Winter",
    "Heroes of Normandie",
    "Mansions of Madness: Second Edition",
    "Carcassonne: Amazonas",
    "Sagrada",
    "Smash Up",
    "Celestia",
    "Discoveries",
    "Ticket to Ride: Märklin",
    "Blood Bowl (fourth edition)",
    "Caverna: The Cave Farmers",
    "BattleLore (Second Edition)",
    "The Great War",
    "Last Night on Earth: The Zombie Game",
    "Cleopatra and the Society of Architects",
    "Quantum",
    "Neuroshima Hex!",
    "Shogun",
    "Power Grid",
    "Queendomino",
    "The Godfather: The Board Game",
    "Champions of Midgard",
    "First Class: All Aboard the Orient Express",
    "Dice Forge",
    "Scythe",
    "Raptor",
    "Ice Cool",
    "Ca$h 'n Guns (second edition)",
    "Twilight Struggle",
    "Pandemic",
    "Spyfall",
    "Yamataï",
    "Captain Sonar",
    "Terraforming Mars",
    "Santorini",
    "Century: Spice Road",
    "Vikingdoms",
    "Dust 1947",
    "Incan Gold",
    "Star Realms",
    "For Sale",
    "Augustus",
    "XenoShyft Onslaught",
    "Tyrants of the Underdark",
    "The Resistance",
    "Nothing Personal",
    "Catan Geographies: Germany",
    "The Manhattan Project",
]

zee = [
    "Pandemic",
    "Onirim",
    "Neuroshima Hex!",
    "7 Wonders Duel",
    "Blue Moon Legends",
    "Ghost Stories",
    "7 Wonders",
    "King of Tokyo",
    "Deus",
    "Deception: Murder in Hong Kong",
    "Rising Sun",
    "Time Stories",
    "Hanamikoji",
    "Fire & Axe: A Viking Saga",
    "Shadows over Camelot",
    "Jamaica",
    "Battlestar Galactica",
    "Colosseum",
    "7 Wonders",
    "Fury of Dracula 3rd Edition",
    "Cosmic Encounter",
    "Jamaica",
    "Yamataï",
    "Arkham Horror: The Card Game",
    "Karuba",
    "Uluru",
    "The Others",
    "Factory Funner",
    "Summoner Wars",
    "Ticket to Ride: Europe",
    "Archaeology: The New Expedition",
    "Abyss",
    "Liar's Dice",
    "Saint Malo",
    "Blue Moon City",
    "Carcassonne: The City",
    "It's Mine",
    "Elysium",
    "Sheep & Thief",
    "San Juan (second edition)",
    "T.I.M.E Stories: The Marcy Case",
    "Blood Rage",
    "Arena: Roma II",
    "Ethnos",
    "Mr. Jack",
    "Tides of Madness",
    "Among the Stars",
    "Raptor",
    "Forbidden Desert",
    "Compatibility",
    "Claustrophobia",
    "Avenue",
    "Bruges",
    "Bärenpark",
    "Libertalia",
    "Mykerinos",
    "Pow Wow",
    "Witness",
    "Gold West",
    "K2",
    "Mission: Red Planet",
    "Las Vegas",
    "Santiago de Cuba",
    "Automania",
    "Thunderbirds",
    "Oceanos",
    "R-Eco",
    "Tintas",
    "Notre Dame",
    "Palazzo",
    "Relic Runners",
    "Onitama",
    "Viceroy",
    "LYNGK",
    "Babel",
    "Dixit",
    "Hive",
    "DVONN",
    "Scythe",
    "Queendomino",
    "Cavemen: The Quest for Fire",
    "Snow Tails",
    "Vegas Showdown",
    "Beasty Bar",
    "Rising 5: Runes of Asteros",
    "Alhambra",
    "Shakespeare",
    "The Pillars of the Earth",
    "Citadels",
    "Quadropolis",
    "Magic: The Gathering",
    "Robinson Crusoe: Adventure on the Cursed Island",
    "Legends of Andor",
    "Cleopatra and the Society of Architects",
    "Dead Men Tell No Tales",
    "Viticulture",
    "Santorini",
    "Friday",
    "Shanghaien",
    "Takenoko",
]
'''
lists = (tom,eric,sam,zee)
master_dict = {}

for lst in lists:
    for i,item in enumerate(lst[:25]):
        if item in master_dict:
            master_dict[item] += 100 - i
        else:
            master_dict[item] = 100 - i

for k, v in sorted(master_dict.items(), key=itemgetter(1),reverse=True):
    print(k)
'''

q = []
calls = 0
seen = set()

def ranked_choice(calls, list_of_lists):
    first = list_of_lists[0]
    second = list_of_lists[1]
    third = list_of_lists[2]

    state = first[0]+second[0]+third[0]
    if state not in seen:
        if first[0] == second[0] or first[0] == third[0]:
            print("Found one",first[0])
            return True
        elif second[0] == third[0]:
            print("Found one",second[0])
            return True
        
        calls += 1

        remove_first = [first[1:],second[:],third[:]]
        remove_second = [first[:],second[1:],third[:]]
        remove_third = [first[:],second[:],third[1:]]
        heapq.heappush(q,(calls, remove_first))
        heapq.heappush(q,(calls, remove_second))
        heapq.heappush(q,(calls, remove_third))

    seen.update((state,))
    ranked_choice(*heapq.heappop(q))


def ranked_choice_v2(calls, list_of_lists):
    num_lists = len(list_of_lists)
    votes_needed = num_lists//2 + 1
    state = []

    for lst in list_of_lists:
        state.append(lst[0])

    if ' '.join(state) not in seen:
        for i,vote in enumerate(state):
            match = 0
            for other in state[1:]:
                if vote == other:
                    match += 1
            if match >= votes_needed:
                print(vote)
                return vote      
        calls += 1
        for i in range(num_lists):
            new_l_of_l = deepcopy(list_of_lists)
            new_l_of_l[i] = new_l_of_l[i][1:]
            heapq.heappush(q,(calls,new_l_of_l))

    seen.update((' '.join(state),))
    ranked_choice_v2(*heapq.heappop(q))

ranked_choice_v2(calls, [tom,eric,zee])

q = []

ranked_choice(calls, [tom,eric,zee])

