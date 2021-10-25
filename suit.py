class Suit:
    """
    Provide information about suits and color
    """
    red = ['hearts' , 'diamonds']
    black = ['clubs' , 'spades']

    def __init__(self, name):
        if name in self.red or name in self.black:
            self.name = name
        else:
            self.name = "INVALID"

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getColor(self):
        if self.name in self.red:
            return 'red'
        elif self.name in self.black:
            return 'black'

        return "INVALID"

    def becomeTrump(self):
        # Called on the left to correct info
        if self.name in self.red:
            self.name = self.red[self.red.index(self.name) - 1]
        else:
            self.name = self.black[self.black.index(self.name) - 1]

def main():
    s = Suit('hearts')
    print(s)
    print('After change')
    s.becomeTrump()
    print(s)

if __name__ == "__main__":
    main()
