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

    def to_string(self):
        ret_str = str(self.value) + " of " + str(self.suit)
        return ret_str

    def get_value(self):
        return self.values[self.value]

    def get_color(self):
        return self.suit.getColor()

    def get_suit(self):
        return self.suit.toString()

    def set_left(self):
        self.value = 'left'
        self.suit.becomeTrump()

    def set_right(self):
        self.value = 'right'


def main():
    my_card = Card('jack', 'hearts')
    print(my_card.getValue())
    print(my_card.getColor())


if __name__ == "__main__":
    main()
