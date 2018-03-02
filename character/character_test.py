from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hola! como te llamas?")
dave.talk()
dave.set_weakness("Sword")
print("What will you gifht with?")
fight_with = input()
dave.fight(fight_with)