from card import Card

class Player:
    """
    Holds the information and cards of a player
    """
    def __init__(self, name):
        self.points = 0
        self.cards = []
        self.name = name

    def getPoints(self):
        return self.points

    def getCards(self):
        return self.cards

    def getName(self):
        return self.name

    def setCards(self, cards):
        self.cards = cards

    def displayCards(self):
        for card in cards:
            print(card)

def main():
    p = Player('Johhny')
    p2 = Player('James')
    print(p.getName())
    print(p2.getName())

if __name__ == __main__():
    main()
