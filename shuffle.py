from card import Card
import random


class Shuffle:
    """
    Shuffle cards and create deck
    """

    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["9", "10", "jack", "queen", "king", "ace"]

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.deck.append(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_deck(self):
        return self.deck

    def print_deck(self):
        for c in self.deck:
            print(c)


def main():
    s = Shuffle()
    s.create_deck()
    s.print_deck()


if __name__ == "__main__":
    main()
