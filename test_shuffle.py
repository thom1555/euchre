import unittest

from shuffle import Shuffle
from card import Card

class TestSuffle(unittest.TestCase):

    def test_deck_size(self):
        s = Shuffle()

        # Should start with empty list
        deck = s.getDeck()
        self.assertEqual(len(deck), 0)

        # Should populate 24 cards
        s.createDeck()
        deck = s.getDeck()
        self.assertEqual(len(deck), 24)

    def test_exists(self):
        # Init deck
        s = Shuffle()
        s.createDeck()
        deck = s.getDeck()

        # Create cards
        jackH = Card('jack', 'hearts')
        tenS = Card('10', 'spades')
        kingD = Card('king', 'diamonds')
        queenC = Card('queen', 'clubs')
