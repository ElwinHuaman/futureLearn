import src
#from room import Room
#from item import Item
#from character import Character, Enemy, Friend

kitchen = src.Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")

dinning_hall = src.Room("DInning Hall")
dinning_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = src.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wc")

kitchen.link_room(dinning_hall, "south") 
dinning_hall.link_room(kitchen, "north") 
dinning_hall.link_room(ballroom, "west") 
ballroom.link_room(dinning_hall, "east")

# ONE enemy
dave = src.Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrrrrsadl.. ertrtg...brains")
dave.set_weakness("cheese")
dinning_hall.set_character(dave)

tabitha = src.Enemy("Tabitha", "An enormous spider with countless eyes")
tabitha.set_conversation("Ssss... I'm so bored...Zzz")
tabitha.set_weakness("book")
kitchen.set_character(tabitha)

#SECOND friend
grill = src.Enemy("Grill", "A fat fish in the Amazonas")
grill.set_conversation("gluglu...blooddd...glu")
grill.set_weakness("water")
ballroom.set_character(grill)

#ITEMS created
cheese = src.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = src.Item("book")
book.set_description("A really good book entitled 'Comentarios Reales'")
dinning_hall.set_item(book)

water = src.Item("water")
water.set_description("A purify water from Peru")
kitchen.set_item(water)

#dining_hall.get_details()
current_room = kitchen    
backpack = []
dead = False

while dead == False:		

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
            print("You put the: " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Upps, there is nothing here to take!")
    elif command == "hug":
        if isinstance(inhabitant, Enemy):
            print("I wouldn't do that if I were you...")
        else:
            inhabitant.hug()
    elif command == "items":
        if not backpack:
            print("You don't have items in you backpack")
        else:
            print("You have these items now: ")
            print(backpack)
    else:
        print("I don't know how to " + command)
# sword = Item("Sword","Small and easy to use in a battle...")
# sword.get_details()
