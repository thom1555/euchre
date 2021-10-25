import unittest

from card import Card

class TestCard(unittest.TestCase):

    def test_card(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.getColor(), 'red')
        self.assertEqual(card.getSuit(), 'hearts')
        self.assertEqual(card.getValue(), 11)

    def test_make_left(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.getSuit(), 'hearts')
        card.setLeft()
        self.assertEqual(card.getSuit(), 'diamonds')
        self.assertEqual(card.getValue(), 15)

    def test_make_right(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.getSuit(), 'hearts')
        card.setRight()
        self.assertEqual(card.getSuit(), 'hearts')
        self.assertEqual(card.getValue(), 16)
