class Flower():
    picked = 0

    def __init__(self):
        #An instance variable, a different copy is stored once per object
        self.color = "red"
    
    def pick(self):
        Flower.picked += 1

    def get_status(self):
        print(str(Flower.picked) + " flowers have been picked")