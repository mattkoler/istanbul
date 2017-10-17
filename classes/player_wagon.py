class PlayerWagon:
    
    def __init__(self, player_number):
        self.coins = 1 + player_number
        self.red = self.yellow = self.green = self.blue = self.gems = 0
        self.item_max = 2
        self.hand = []
        self.assistants = 4
        self.location = 7 #7 is the fountain
        self.assist_locs = [] #empty because all with player atm
        self.red_building = self.yellow_building = self.green_building = self.blue_building = False
    
    def add_lira(self, lira):
        self.coins += lira
        
    def remove_lira(self, lira):
        if self.coins < lira:
            return False
        self.coins -= lira
        return True
    
    def fill_red(self):
        self.red = self.item_max
    
    def fill_yellow(self):
        self.yellow = self.item_max
        
    def fill_green(self):
        self.green = self.item_max
        
    def add_red(self):
        self.red = min(self.red+1, self.item_max)
        
    def add_yellow(self):
        self.yellow = min(self.yellow+1, self.item_max)
        
    def add_green(self):
        self.green = min(self.green+1, self.item_max)
    
    def add_blue(self):
        self.blue = min(self.blue+1, self.item_max)
        
    def add_gem(self):
        self.gems += 1
        
    def remove_red(self):
        if self.red <= 0:
            return False
        self.red -= 1
    
    def remove_yellow(self):
        if self.yellow <= 0:
            return False
        self.yellow -= 1   
    
    def remove_green(self):
        if self.green <= 0:
            return False
        self.green -= 1

    def remove_blue(self):
        if self.blue <= 0:
            return False
        self.blue -= 1
        
    def add_capacity(self):
        if self.item_max >= 5:
            return False
        self.item_max += 1

    def remove_assistant(self):
        if self.assistants > 0:
            self.assistants -= 1
            return True
        return False

    def add_assistant(self):
        self.assistants += 1

    def get_assistants(self):
        return self.assistants

    def get_resources(self):
        #returns a list of resources [red, yellow, green, blue]
        return [self.red,self.yellow,self.green,self.blue]

    def get_coins(self):
        return self.coins

    def get_player_loc(self):
        return self.location

    def get_assistant_loc(self):
        return self.assist_locs

    def check_resources(self, resources):
        """Takes in a list of single letter lower case resources to check ['r','g','b','b'] and returns True/False"""
        if self.red < resources.count('r'):
            return False
        if self.green < resources.count('g'):
            return False
        if self.yellow < resources.count('y'):
            return False
        if self.blue < resources.count('b'):
            return False
        return True


    

