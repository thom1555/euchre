import unittest

from card import Card
from random_ai import RandomAi


def is_card(played):
    to_return = False
    if played is not None:
        if played.get_color() == 'red':
            to_return = True
        elif played.get_color() == 'black':
            to_return = True

    return to_return


class MyTestCase(unittest.TestCase):

    def test_no_cards_exception(self):
        r1 = RandomAi("Puff")
        with self.assertRaises(Exception) as context:
            r1.pick_card()
        self.assertTrue('Player has no cards!' in str(context.exception))

    def test_play_card(self):
        r1 = RandomAi("Snake")
        r1.set_cards([Card('jack', 'hearts'), Card('jack', 'diamonds'), Card('ace', 'hearts'), Card('king', 'hearts'),
                      Card('queen', 'hearts')])
        selected = r1.pick_card()
        self.assertTrue(is_card(selected))


if __name__ == '__main__':
    unittest.main()
