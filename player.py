from card import Card


class Player:
    """
    Holds the information and cards of a player
    """

    def __init__(self, name):
        self.tricks = 0
        self.cards = []
        self.name = name
        self.called_trump = False
        self.times_euchred = 0

    def get_tricks(self):
        return self.tricks

    def get_cards(self):
        return self.cards

    def get_name(self):
        return self.name

    def get_times_euchred(self):
        return self.times_euchred

    def get_called_trump(self):
        return self.called_trump

    def set_cards(self, cards):
        self.cards = cards

    def display_cards(self):
        for card in self.cards:
            print(card)

    def add_trick(self):
        self.tricks += 1

    def add_euchre(self):
        self.times_euchred += 1

    def set_called_trump(self):
        self.called_trump = True

    def reset(self):
        self.called_trump = False
        self.cards = []
        self.tricks = 0


def main():
    p = Player('Rick')
    cards = [Card('jack', 'hearts'), Card('jack', 'diamonds'), Card('ace', 'hearts'), Card('king', 'hearts'),
             Card('queen', 'hearts')]
    p.set_cards(cards)

    print(p.get_name())
    p.display_cards()


if __name__ == "__main__":
    main()
