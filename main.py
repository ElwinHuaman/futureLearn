from room import Room
from item import Item
from character import Enemy
from character import Friend

kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")

dinning_hall = Room("DInning Hall")
dinning_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wc")

kitchen.link_room(dinning_hall, "south") 
dinning_hall.link_room(kitchen, "north") 
dinning_hall.link_room(ballroom, "west") 
ballroom.link_room(dinning_hall, "east")

# ONE enemy
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrrrrsadl.. ertrtg...brains")
dave.set_weakness("cheese")
dinning_hall.set_character(dave)
#SECOND enemy
grill = Friend("Grill", "A fat fish")
grill.set_conversation("Como te ayudo")
ballroom.set_character(grill)

#dining_hall.get_details()
current_room = kitchen    
dead = False

while dead == False:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        #move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one here to fight with")
        else:
            print("What will you gifht with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                #What happends if you win?
                print("Congratulation!!! you can go to next room")
                current_room.character = None
            else:
                #What happens if you lose
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                dead = True
    elif command == "hug":
        if isinstance(inhabitant, Enemy):
            print("I wouldn't do that if I were you...")
        else:
            inhabitant.hug()
# sword = Item("Sword","Small and easy to use in a battle...")
# sword.get_details()
