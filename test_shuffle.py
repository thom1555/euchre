import unittest

from shuffle import Shuffle
from card import Card


class TestShuffle(unittest.TestCase):

    def test_deck_size(self):
        s = Shuffle()
        deck = s.get_deck()  # Should populate 24 cards
        self.assertEqual(len(deck), 24)

    def test_exists_jack_hearts(self):
        s = Shuffle()
        deck = s.get_deck()
        jack_hearts = Card('jack', 'hearts')

        contains = False
        for c in deck:
            if c.to_string() == jack_hearts.to_string():
                contains = True
                break
        self.assertTrue(contains)

    def test_exists_2(self):
        s = Shuffle()
        deck = s.get_deck()
        ten_spades = Card('10', 'spades')

        contains = False
        for c in deck:
            if c.to_string() == ten_spades.to_string():
                contains = True
                break
        self.assertTrue(contains)

    def test_exists_3(self):
        s = Shuffle()
        deck = s.get_deck()
        king_diamonds = Card('king', 'diamonds')

        contains = False
        for c in deck:
            if c.to_string() == king_diamonds.to_string():
                contains = True
                break
        self.assertTrue(contains)

    def test_exists_4(self):
        s = Shuffle()
        deck = s.get_deck()
        queen_clubs = Card('queen', 'clubs')

        contains = False
        for c in deck:
            if c.to_string() == queen_clubs.to_string():
                contains = True
                break
        self.assertTrue(contains)
