class player_wagon:
    
    def __init__(self, coins):
        self.coins = coins
        self.red = self.yellow = self.green = self.blue = self.gems = 0
        self.item_max = 2
    
    def add_lira(self, lira):
        self.coins += lira
        
    def remove_lira(self, lira):
        if self.coins < lira:
            return False
        self.coins -= lira
    
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
