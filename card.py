from suit import Suit


class Card:
    """
    Provide value information and other aspects of a card
    """
    values = {'9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14, 'left': 15, 'right': 16}

    def __init__(self, value, suit):
        self.suit = Suit(suit)
        self.value = value

    def __str__(self):  # pragma: no cover
        return self.to_string()

    def __repr__(self):  # pragma: no cover
        return self.to_string()

    def to_string(self):
        ret_str = str(self.value) + " of " + str(self.suit)
        return ret_str

    def get_value(self):
        return self.values[self.value]

    def get_color(self):
        return self.suit.get_color()

    def get_suit(self):
        return self.suit.to_string()

    def set_left(self):
        self.value = 'left'
        self.suit.become_trump()

    def set_right(self):
        self.value = 'right'

    def is_black_jack(self):
        if self.value == 'jack' and self.suit.get_color() == 'black':
            return True
        return False


def main():  # pragma: no cover
    my_card = Card('jack', 'hearts')
    print(my_card.get_value())
    print(my_card.get_color())


if __name__ == "__main__":  # pragma: no cover
    main()
