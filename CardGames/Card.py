class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def show(self):
        print("{} of {}".format(self.face, self.suit))


    