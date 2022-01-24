from suit import Suit
from card_value import CardValue


class Card:
    """
    Provide value information and other aspects of a card
    """

    def __init__(self, point_value, suit):
        self.suit = Suit(suit)
        self.point_value = CardValue[point_value]

    def __str__(self):  # pragma: no cover
        return self.to_string()

    def __repr__(self):  # pragma: no cover
        return self.to_string()

    def to_string(self):
        ret_str = str(self.point_value) + " of " + str(self.suit)
        return ret_str

    def get_point_value(self):
        return self.point_value.value

    def get_color(self):
        return self.suit.get_color()

    def get_suit(self):
        return self.suit.to_string()

    def set_left(self):
        self.point_value = 'LEFT'
        self.suit.become_trump()

    def set_right(self):
        self.point_value = 'RIGHT'

    def is_black_jack(self):
        if self.point_value == 'JACK' and self.suit.get_color() == 'BLACK':
            return True
        return False


def main():  # pragma: no cover
    my_card = Card('JACK', 'hearts')
    print(my_card.get_point_value())
    print(my_card.get_color())


if __name__ == "__main__":  # pragma: no cover
    main()
