from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies.")
kitchen.get_description()
kitchen.describe()

dining_hall = Room("DInning Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

kitchen.linked_rooms(dining_hall,"south")