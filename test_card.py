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

    def test_not_black_jack(self):
        card_1 = Card('jack', 'hearts')
        card_2 = Card('10', 'spades')
        card_3 = Card('11', 'diamonds')

        self.assertFalse(card_1.is_black_jack())
        self.assertFalse(card_2.is_black_jack())
        self.assertFalse(card_3.is_black_jack())

    def test_is_black_jack(self):
        spades = Card('jack', 'spades')
        clubs = Card('jack', 'clubs')

        self.assertTrue(clubs.is_black_jack())
        self.assertTrue(spades.is_black_jack())
