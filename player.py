from card import Card


class Player:
    """
    Holds the information and cards of a player
    """

    def __init__(self, name):
        self.points = 0
        self.cards = []
        self.name = name

    def get_points(self):
        return self.points

    def get_cards(self):
        return self.cards

    def get_name(self):
        return self.name

    def set_cards(self, cards):
        self.cards = cards

    def display_cards(self):
        for card in self.cards:
            print(card)


def main():
    p = Player('Johhny')
    cards = [Card('jack', 'hearts'), Card('jack', 'diamonds'), Card('ace', 'hearts'), Card('king', 'hearts'),
             Card('queen', 'hearts')]
    p.set_cards(cards)

    print(p.get_name())
    p.display_cards()


if __name__ == "__main__":
    main()
