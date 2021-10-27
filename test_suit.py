import unittest

from suit import Suit


class TestSuit(unittest.TestCase):

    def test_suit_color(self):
        h = Suit('hearts')
        c = Suit('clubs')
        d = Suit('diamonds')
        s = Suit('spades')
        x = Suit('bad info :()')
        self.assertEqual(h.get_color(), 'red')
        self.assertEqual(c.get_color(), 'black')
        self.assertEqual(d.get_color(), 'red')
        self.assertEqual(s.get_color(), 'black')
        self.assertEqual(x.get_color(), 'INVALID')

    def test_suit_change(self):
        # Hearts to diamonds
        h = Suit('hearts')
        self.assertEqual(h.to_string(), 'hearts')
        h.become_trump()
        self.assertEqual(h.to_string(), 'diamonds')

        # Diamonds to hearts
        d = Suit('diamonds')
        self.assertEqual(d.to_string(), 'diamonds')
        d.become_trump()
        self.assertEqual(d.to_string(), 'hearts')

        # Spades to clubs
        s = Suit('spades')
        self.assertEqual(s.to_string(), 'spades')
        s.becomeTrump()
        self.assertEqual(s.toString(), 'clubs')

        # Clubs to Spades
        c = Suit('clubs')
        self.assertEqual(c.toString(), 'clubs')
        c.becomeTrump()
        self.assertEqual(c.toString(), 'spades')
