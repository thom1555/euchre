import unittest

from card import Card


class TestCard(unittest.TestCase):

    def test_card(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.get_color(), 'red')
        self.assertEqual(card.get_suit(), 'hearts')
        self.assertEqual(card.get_value(), 11)

    def test_card_2(self):
        card = Card('10', 'spades')
        self.assertEqual(card.get_color(), 'black')
        self.assertEqual(card.get_suit(), 'spades')
        self.assertEqual(card.to_string(), "10 of spades")
        self.assertEqual(card.get_value(), 10)

    def test_make_left(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.get_suit(), 'hearts')
        card.set_left()
        self.assertEqual(card.get_suit(), 'diamonds')
        self.assertEqual(card.get_value(), 15)

    def test_make_right(self):
        card = Card('jack', 'hearts')
        self.assertEqual(card.get_suit(), 'hearts')
        card.set_right()
        self.assertEqual(card.get_suit(), 'hearts')
        self.assertEqual(card.get_value(), 16)
