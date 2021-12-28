from player import Player
from card import Card
from suit import Suit
from team import Team
from shuffle import Shuffle


class Game:
    def __init__(self, name_one, name_two, name_three, name_four, team_one, team_two):
        self.shuffle = Shuffle()
        self.players = [Player(name_one), Player(name_two), Player(name_three), Player(name_four)]
        self.team_one = Team(team_one, self.players[0], self.players[2])
        self.team_two = Team(team_two, self.players[1], self.players[3])
        self.dealer = 0
        self.trump = Suit.spades
        self.flipped_card = None

    def black_jack(self):
        count = 0
        for card in self.shuffle.get_deck():
            if card.is_black_jack():
                return count % 4
            count += 1

    def select_trump(self):
        pass

    def deal(self):
        index = 0
        self.shuffle.shuffle_deck()
        deck = self.shuffle.get_deck()
        for player in self.players:
            player.set_cards(deck[index:(index+5)])
            index += 5

    def start_game(self):
        self.shuffle.shuffle_deck()
        self.dealer = self.black_jack()
        self.deal()
        self.display_cards()

    def display_cards(self):
        for player in self.players:
            print(player.get_name())
            print(player.get_cards())


def main():  # pragma: no cover
    new_game = Game('Puff', 'Snake', 'Voldie', 'Binx', 'Ballers', 'Scrubs')
    new_game.start_game()


if __name__ == "__main__":  # pragma: no cover
    main()
