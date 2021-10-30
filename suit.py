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
            self.name = "INVALID"

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        return self.name

    def get_color(self):
        if self.name in self.red:
            return 'red'
        elif self.name in self.black:
            return 'black'

        return "INVALID"

    def become_trump(self):
        # Called on the left to correct info
        if self.name in self.red:
            self.name = self.red[self.red.index(self.name) - 1]
        else:
            self.name = self.black[self.black.index(self.name) - 1]


def main():
    s = Suit('hearts')
    print(s)
    print('After change')
    s.become_trump()
    print(s)


if __name__ == "__main__":
    main()