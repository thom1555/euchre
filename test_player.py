import unittest

from card import Card
from player import Player
from suit import Suit


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

    def test_play_card(self):
        c1 = Card('jack', 'hearts')
        c2 = Card('jack', 'diamonds')
        c3 = Card('ace', 'hearts')
        c4 = Card('king', 'hearts')
        c5 = Card('queen', 'hearts')

        p = Player("Puff")
        p.set_cards([c1, c2, c3, c4, c5])
        self.assertEqual(len(p.get_cards()), 5)
        p.play_card(c2)
        self.assertEqual(len(p.get_cards()), 4)

        contains = c1 in p.get_cards()
        self.assertEqual(contains, True)
        contains = c2 in p.get_cards()
        self.assertEqual(contains, False)

    def test_legal_moves(self):
        p = Player("Puff")
        p.set_cards([Card('jack', 'hearts'), Card('jack', 'diamonds'), Card('ace', 'hearts'), Card('king', 'hearts'),
                     Card('queen', 'hearts')])

        moves = p.get_legal_moves(Suit.spades)
        self.assertEqual(len(moves), 5)
        moves = p.get_legal_moves(Suit.hearts)
        self.assertEqual(len(moves), 4)
        moves = p.get_legal_moves(Suit.diamonds)
        self.assertEqual(len(moves), 1)
        moves = p.get_legal_moves(Suit.clubs)
        self.assertEqual(len(moves), 5)


if __name__ == '__main__':
    unittest.main()
