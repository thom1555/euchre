from card import Card
import random

class Shuffle:
    """
    Shuffle cards and create deck
    """
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["9", "10", "jack", "queen", "king", "ace"]

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.deck.append(card)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def getDeck(self):
        return self.deck

    def printDeck(self):
        for c in self.deck:
            print(c)


def main():
    s = Shuffle()
    s.createDeck()
    s.printDeck()

if __name__ == "__main__":
    main()
