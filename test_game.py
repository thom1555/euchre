import unittest

from game import Game
from suit import Suit


class TestGame(unittest.TestCase):
    def test_setup(self):
        g = Game('tim', 'rick', 'bob', 'james', 'ballers', 'scrubs')
        self.assertEqual(len(g.players), 4)
        self.assertEqual(g.dealer, 0)
        self.assertEqual(g.trump, Suit.spades)


if __name__ == '__main__':
    unittest.main()
