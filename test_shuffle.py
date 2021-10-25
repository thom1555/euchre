import unittest

from shuffle import Shuffle
from card import Card

class TestSuffle(unittest.TestCase):

    def test_deck_size(self):
        s = Shuffle()
        deck = s.getDeck()  # Should populate 24 cards
        self.assertEqual(len(deck), 24)
        

    def test_exists_jack_hearts(self):
        s = Shuffle()
        deck = s.getDeck()
        jackH = Card('jack', 'hearts')

        contains = False
        for c in deck:
            if c.toString() == jackH.toString():
                contains = True
                break
        self.assertTrue(contains)


    def test_exists_2(self):
        s = Shuffle()
        deck = s.getDeck()
        tenS = Card('10', 'spades')

        contains = False
        for c in deck:
            if c.toString() == tenS.toString():
                contains = True
                break
        self.assertTrue(contains)


    def test_exists_3(self):
        s = Shuffle()
        deck = s.getDeck()
        kingD = Card('king', 'diamonds')

        contains = False
        for c in deck:
            if c.toString() == kingD.toString():
                contains = True
                break
        self.assertTrue(contains)


    def test_exists_4(self):
        s = Shuffle()
        deck = s.getDeck()
        queenC = Card('queen', 'clubs')

        contains = False
        for c in deck:
            if c.toString() == queenC.toString():
                contains = True
                break
        self.assertTrue(contains)
