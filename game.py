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
        pass