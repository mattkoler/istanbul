

def start_game():
    num_players = int(input("How many players? (2-5): "))
    colors = ['(W)hite', '(G)reen', '(R)ed', '(B)lue', '(P)urple']
    p_colors = []
    for _ in range(num_players):
        choice = input("What color could you like to choose? {} :".format(str(colors)))
        p_colors.append(choice)
    print("You chose {} players with the colors {}.".format(num_players,str(p_colors)))

start_game()