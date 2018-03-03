class Item():
    def __init__(self, name):
        self.name = name
        self.description = None
    
    def set_name(self, item_name):
        self.name = item_name
    def get_name(self):
        return self.name
    
    def set_description(self, item_description):
        self.description = item_description
    def get_description(self):
        return self.description
    
    def get_details(self):
        print("Name: "+self.name)
        print("Description: "+ self.description)