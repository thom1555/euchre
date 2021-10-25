import unittest

from player import Player

class TestSuit(unittest.TestCase):

    def test_player_name(self):
        p1 = Player('Johhny')
        p2 = Player('Jimmy')

        self.assertEqual(p1.getName(), 'Johhny')
        self.assertEqual(p2.getName(), 'Jimmy')
