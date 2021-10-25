import unittest

from suit import Suit

class TestSuit(unittest.TestCase):

    def test_suit_color(self):
        h = Suit('hearts')
        c = Suit('clubs')
        d = Suit('diamonds')
        s = Suit('spades')
        x = Suit('bad info :()')
        self.assertEqual(h.getColor(), 'red')
        self.assertEqual(c.getColor(), 'black')
        self.assertEqual(d.getColor(), 'red')
        self.assertEqual(s.getColor(), 'black')
        self.assertEqual(x.getColor(), 'INVALID')

    def test_suit_change(self):
        # Hearts to diamonds
        h = Suit('hearts')
        self.assertEqual(h.toString(), 'hearts')
        h.becomeTrump()
        self.assertEqual(h.toString(), 'diamonds')

        # Diamonds to hearts
        d = Suit('diamonds')
        self.assertEqual(d.toString(), 'diamonds')
        d.becomeTrump()
        self.assertEqual(d.toString(), 'hearts')

        # Spades to clubs
        s = Suit('spades')
        self.assertEqual(s.toString(), 'spades')
        s.becomeTrump()
        self.assertEqual(s.toString(), 'clubs')

        # Clubs to Spades
        c = Suit('clubs')
        self.assertEqual(c.toString(), 'clubs')
        c.becomeTrump()
        self.assertEqual(c.toString(), 'spades')
