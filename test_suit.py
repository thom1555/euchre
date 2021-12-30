import unittest

from suit import Suit


class TestSuit(unittest.TestCase):

    def test_suit_color(self):
        h = Suit('hearts')
        c = Suit('clubs')
        d = Suit('diamonds')
        s = Suit('spades')

        self.assertEqual(h.get_color(), 'red')
        self.assertEqual(c.get_color(), 'black')
        self.assertEqual(d.get_color(), 'red')
        self.assertEqual(s.get_color(), 'black')

    def test_invalid_suit(self):
        with self.assertRaises(Exception) as context:
            x = Suit('bad info :()')
        self.assertTrue('Card is invalid!' in str(context.exception))

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
        s.become_trump()
        self.assertEqual(s.to_string(), 'clubs')

        # Clubs to Spades
        c = Suit('clubs')
        self.assertEqual(c.to_string(), 'clubs')
        c.become_trump()
        self.assertEqual(c.to_string(), 'spades')


if __name__ == '__main__':
    unittest.main()
