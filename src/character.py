class Character():

    def __init__(self, char_name, char_description):
        """Define the constructor"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Returns the description of the character"""
        print("CAUTION!! "+ self.name+" is here!... "+self.description)
        print("and my vulnerabilty is "+ self.get_weakness())
    
    def set_conversation(self, conversation):
        """Set the conversation for the character"""
        self.conversation = conversation
    
    def talk(self):
        """define the method TALK for the characters"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + "doesn't want to talk to you ")
    
    def fight(self, combat_item):
        """The figh method for the class"""
        print(self.name + " doesn't want to fight with you ")
        return True

class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        """The constructor like the main Class"""
        super().__init__(char_name, char_description)
        """mainly for our main class character"""
        self.weakness = None
    
    def set_weakness(self, weakness):
        """Configure or set the weakness of the Enemy character"""
        self.weakness = weakness
    def get_weakness(self):
        """Returns the weakness for the Enemy Character"""
        return self.weakness
    
    def set_enemies_defeated(self, new_enemies_defeated):
        """Set the class variable enemies_defeated"""
        Enemy.enemies_defeated += new_enemies_defeated
    def get_enemies_defeated(self):
        """Returns the enemies_defeated"""
        return Enemy.enemies_defeated

    def fight(self, combat_item):
        """Returns TRUE or FALSE about the fight"""
        if combat_item == self.weakness:
            print("You fend " + self.name + "off with the "+ combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    
    def steal(self):
        """Someone can steal the item"""
        print("You steal from " + self.name)
        #How will you decide what this character has to steal?

class Friend(Character):
    """Is not completed this method, but you can use it and improve the method"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    
    def hug(self):
        print(self.name + " Hug you back!")
    
    def get_gift(self):
        print("You have a poison now ")