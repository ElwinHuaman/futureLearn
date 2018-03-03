from room import Room
from item import Item
from character import Character, Enemy, Friend

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

tabitha = Enemy("Tabitha", "An enormous spider with countless eyes")
tabitha.set_conversation("Ssss... I'm so bored...Zzz")
tabitha.set_weakness("book")
kitchen.set_character(tabitha)

#SECOND friend
grill = Friend("Grill", "A fat fish")
grill.set_conversation("Como te ayudo")
ballroom.set_character(grill)

#ITEMS created
cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Comentarios Reales'")
dinning_hall.set_item(book)

#dining_hall.get_details()
current_room = kitchen    
backpack = []
dead = False

while dead == False:		

    if inhabitant.enemies_defeated >= 5:
        print("You are the Winner!!!!")
        break

    print("\n")         
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    item = current_room.get_item()
    if item is not None:
        item.get_details()

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
            if fight_with in backpack:
                print("you can use it")
                if inhabitant.fight(fight_with) == True:
                    #What happends if you win?
                    print("Congratulation!!! you can go to next room")
                    current_room.character = None
                    if inhabitant.get_enemies_defeated() == 2:
                        print("Congratulations, you have vanquished the enemies")
                        dead = True
                else:
                    #What happens if you lose
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have this item yet.."+ fight_with)
            
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + "in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Upps, there is nothing here to take!")
    elif command == "hug":
        if isinstance(inhabitant, Enemy):
            print("I wouldn't do that if I were you...")
        else:
            inhabitant.hug()
    else:
        print("I don't know how to " + command)
# sword = Item("Sword","Small and easy to use in a battle...")
# sword.get_details()
