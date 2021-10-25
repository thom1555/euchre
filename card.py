from suit import Suit

class Card:
    """
    Provide value information and other aspects of a card
    """
    values = {'9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14, 'left': 15, 'right': 16}

    def __init__(self, value, suit):
        self.suit = Suit(suit)
        self.value = value

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def toString(self):
        returnString = str(self.value) + " of " + str(self.suit)
        return returnString

    def getValue(self):
        return self.values[self.value]

    def getColor(self):
        return self.suit.getColor()

    def getSuit(self):
        return self.suit.toString()

    def setLeft(self):
        self.value = 'left'
        self.suit.becomeTrump()

    def setRight(self):
        self.value = 'right'


def main():
    myCard = Card('jack', 'hearts')
    print(myCard.getValue())
    print(myCard.getColor())

if __name__ == "__main__":
    main()
