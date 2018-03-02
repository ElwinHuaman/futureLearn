class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name + " is here! ")
        print(self.description)
    
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + "doesn't want to talk to you ")
    
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you ")
        return True

class Enemy(Character):

enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def set_weakness(self, weakness):
        self.weakness = weakness
    def get_weakness(self):
        return self.weakness
    
    def set_enemies_defeated(self, new_enemies_defeated):
        Enemy.enemies_defeated = new_enemies_defeated
    def get_enemies_defeated(self):
        return Enemy.enemies_defeated

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + "off with the "+ combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    
    def steal(self):
        print("You steal from " + self.name)
        #How will you decide what this character has to steal?

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    
    def hug(self):
        print(self.name + " Hug you back!")
    
    def get_gift(self):
        print("You have a poison now ")