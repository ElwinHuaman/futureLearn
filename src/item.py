class Item():
    """Allows create items like chees, water, etc for the rooms"""
    def __init__(self, name):
        """Define the constructor"""
        self.name = name
        self.description = None
    
    """Define the setter and getter for atributte name"""
    def set_name(self, item_name):
        self.name = item_name
    def get_name(self):
        return self.name

    """Define the setter and getter for atributte description"""
    def set_description(self, item_description):
        self.description = item_description
    def get_description(self):
        return self.description
    
    def get_details(self):
        """Describe the item"""
        print("ATENTION!!..there is an special ITEM to kill zombies|monsters and more")
        print("Name of the Item: '"+self.name + "' Useful for "+ self.description)