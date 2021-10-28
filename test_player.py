import unittest

from card import Card
from player import Player


class TestSuit(unittest.TestCase):

    def test_player_name(self):
        p1 = Player('Johny')
        p2 = Player('Jimmy')

        self.assertEqual(p1.get_name(), 'Johny')
        self.assertEqual(p2.get_name(), 'Jimmy')

    def test_player_tricks(self):
        p1 = Player('Bill')
        self.assertEqual(p1.get_tricks(), 0)

        p1.add_trick()
        self.assertEqual(p1.get_tricks(), 1)

    def test_player_euchred(self):
        p1 = Player("Timmy")
        self.assertEqual(p1.get_times_euchred(), 0)

        p1.add_euchre()
        self.assertEqual(p1.get_times_euchred(), 1)

    def test_called_trump(self):
        p1 = Player("Puff")
        self.assertEqual(p1.get_called_trump(), False)

        p1.set_called_trump()
        self.assertTrue(p1.get_called_trump())

    def test_reset(self):
        p1 = Player("Jeremy")
        p1.set_cards([Card('jack', 'hearts'), Card('jack', 'diamonds'), Card('ace', 'hearts'), Card('king', 'hearts'),
                      Card('queen', 'hearts')])
        p1.add_trick()
        p1.set_called_trump()

        p1.reset()
        self.assertEqual(p1.get_cards(), [])
        self.assertEqual(p1.get_called_trump(), False)
        self.assertEqual(p1.get_tricks(), 0)


