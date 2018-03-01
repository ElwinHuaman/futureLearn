from room import Room
from item import Item

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

#dining_hall.get_details()
# current_room = kitchen          

# while True:		
#     print("\n")         
#     current_room.get_details()         
#     command = input("> ")    
#     current_room = current_room.move(command)

# sword = Item("Sword","Small and easy to use in a battle...")
# sword.get_details()