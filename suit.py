class Suit:
    """
    Provide information about suits and color
    """
    hearts = 'hearts'
    clubs = 'clubs'
    diamonds = 'diamonds'
    spades = 'spades'
    red = ['hearts', 'diamonds']
    black = ['clubs', 'spades']

    def __init__(self, name):
        if name in self.red or name in self.black:
            self.name = name
        else:
            raise Exception('Card is invalid!')

    def __str__(self):  # pragma: no cover
        return self.to_string()

    def __repr__(self):  # pragma: no cover
        return self.to_string()

    def to_string(self):
        return self.name

    def get_color(self):
        if self.name in self.red:
            return 'RED'
        return 'BLACK'

    def become_trump(self):
        # Called on the left to correct info
        if self.name in self.red:
            self.name = self.red[self.red.index(self.name) - 1]
        else:
            self.name = self.black[self.black.index(self.name) - 1]


def main():  # pragma: no cover
    s = Suit('hearts')
    print(s)
    print('After change')
    s.become_trump()
    print(s)


if __name__ == "__main__":  # pragma: no cover
    main()