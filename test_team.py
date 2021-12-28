import unittest

from player import Player
from team import Team
from points import Points


class TestTeam(unittest.TestCase):

    def test_name(self):
        players = [Player("Snake"), Player("Puff"), Player("Voldie"), Player("Goose")]
        team_one = Team("Ballers", players[0], players[2])
        team_two = Team("Scrubs", players[1], players[3])
        self.assertEqual(team_one.get_team_name(), "Ballers")
        self.assertEqual(team_two.get_team_name(), "Scrubs")

    def test_points(self):
        players = [Player("Snake"), Player("Puff"), Player("Voldie"), Player("Goose")]
        team_one = Team("Ballers", players[0], players[2])
        team_two = Team("Scrubs", players[1], players[3])
        self.assertEqual(team_one.get_points(), 0)
        self.assertEqual(team_two.get_points(), 0)

        team_one.add_points(Points.ALL_TRICKS.value)
        team_two.add_points(Points.EUCHRE.value)
        self.assertEqual(team_one.get_points(), 2)
        self.assertEqual(team_two.get_points(), 2)


if __name__ == '__main__':
    unittest.main()
