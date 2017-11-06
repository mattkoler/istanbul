def input_from_list(question, answer):
    """Takes in a question and makes sure the user input (ui) is
    contained within the list of answer"""
    ui = input(question).lower()
    while ui not in list(ans.lower() for ans in answer):
        print("Sorry, please choose from: {}".format(", ".join(answer)))
        ui = input(question).lower()
    return ui

def input_int_range(question, low, high):
    """Takes in a question and makes sure the user input (ui) is withing
    a range of ints from low to high inclusive"""
    while True:
        ui = input(question)
        try:
            ui = int(ui)
        except ValueError:
            print("Please enter an integer.")
            continue
        if ui < low or ui > high:
            print("Please enter a value between {} and {}.".format(low, high))
        else:
            break
    return ui

def input_yes_no(question):
    """Takes in a question and returns True if user input (ui) is yes
    and False if ui is no"""
    ui = input(question).lower()
    while ui not in ['yes', 'y', 'no', 'n']:
        print("Please choose yes or no")
        ui = input(question).lower()
    return ui[0] == 'y'
