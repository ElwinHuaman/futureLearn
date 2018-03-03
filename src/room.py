class Room():

    def __init__(self, room_name):
        """Define the constructor of the class Room"""
        self.name = room_name
        self.description = None 
        self.linked_rooms = {}
        self.character = None
        self.item = None
    
    def set_description(self, room_description):
        """Define the setter of description """
        self.description = room_description
    def get_description(self):
        """Define the getter of description, returns the description"""
        return self.description

    def set_name(self, room_name):
        """Define the setter for the name"""
        self.name = room_name
    def get_name(self):
        """return the name by the ggetter method """
        return self.name
        
    def set_character(self, new_character):
        """Define the setter for character"""
        self.character = new_character
    def get_character(self):
        """Define the getter for character"""
        return self.character

    def set_item(self, new_item):
        """Define the setter for item"""
        self.item = new_item
    def get_item(self):
        """Define the getter for item"""
        return self.item 

    def describe(self):
        """Describe the room description"""
        print(self.description)
    
    def link_room(self, room_to_link, direction):
        """Link the rooms each others, some room to others"""
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms: "+ repr(self.linked_rooms))
    
    def get_details(self):
        """Describe the details for the room, the character """
        print("The "+self.name)
        print("-----------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]            
            print("The "+ room.get_name()+" is " + direction)
    
    def move(self, direction):
        """Define the navigation between rooms """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way ")
            return self