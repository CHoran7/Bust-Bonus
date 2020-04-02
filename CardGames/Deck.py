import random

class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def show(self):
        print("{} of {}".format(self.face, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
   
class Game:
    def __init__(self, deck):
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []
        self.stack4 = []
        self.stack5 = []
        self.stack6 = []
        self.stack7 = []
        self.table = []
        self.build()

    def build(self):
        firstCard = deck.drawCard()
        self.stack1.append(firstCard)
    
deck = Deck()
deck.shuffle()
deck.show()
game = Game(deck)
game.build()
