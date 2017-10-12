class tile:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.action = None
        self.merchants = []
        self.assistants = []
        self.family_members = []
        self.governor = False
        self.smuggler = False
        
    def get_merchants(self):
        merchs = ''
        for m in self.merchants:
            merchs += m + ' '
        return merchs
    
    def get_assistants(self):
        assist = ''
        for a in self.assistants:
            assist += a + ' '
        return assist
