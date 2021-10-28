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

    def start_game(self):
        self.shuffle.shuffle_deck()
        print(self.black_jack())

    def black_jack(self):
        count = 0
        for card in self.shuffle.get_deck():
            if card.is_black_jack():
                return count % 4
            count += 1


def main():
    new_game = Game('Puff', 'Snake', 'Voldie', 'Binx', 'Ballers', 'Scrubs')
    new_game.start_game()


if __name__ == "__main__":
    main()
