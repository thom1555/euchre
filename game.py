from player import Player
from card import Card
from team import Team
from shuffle import Shuffle


class Game:
    def __init__(self, name_one, name_two, name_three, name_four, team_one, team_two):
        self.shuffle = Shuffle()
        self.player_one = Player(name_one)
        self.player_two = Player(name_two)
        self.player_three = Player(name_three)
        self.player_four = Player(name_four)
        self.team_one = Team(team_one, self.player_one, self.player_two)
        self.team_two = Team(team_two, self.player_three, self.player_four)
        self.dealer = 0

    def black_jack(self):
        count = 0
        for card in self.shuffle.get_deck():
            if card.is_black_jack():
                return count % 4
            count += 1

    def deal(self):
        self.shuffle.shuffle_deck()
        deck = self.shuffle.get_deck()
        self.player_one.set_cards(deck[0:5])
        self.player_two.set_cards(deck[5:10])
        self.player_three.set_cards(deck[10:15])
        self.player_four.set_cards(deck[15:20])

    def start_game(self):
        self.shuffle.shuffle_deck()
        self.dealer = self.black_jack()
        self.deal()


def main():
    new_game = Game('Puff', 'Snake', 'Voldie', 'Binx', 'Ballers', 'Scrubs')
    new_game.start_game()


if __name__ == "__main__":
    main()
