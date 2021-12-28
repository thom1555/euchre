from player import Player
from suit import Suit

import random


class RandomAi(Player):

    def pick_card(self):
        options = self.get_legal_moves(Suit.clubs)
        if not options:
            raise Exception('Player has no cards!')

        index = random.randint(0, len(options)) - 1
        return options[index]


def main():
    ai = RandomAi('James')
    print(ai.get_name())


if __name__ == "__main__":
    main()
