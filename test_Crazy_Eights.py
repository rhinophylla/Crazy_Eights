import unittest
import itertools
import random

def card_deck():
    """Create list of 52 tuples representing standard playing cards."""
    deck = list(itertools.product(
    ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'],
    ['Spades', 'Hearts', 'Diamonds', 'Clubs']))
    random.shuffle(deck)
    return deck


def calculate_points(player_hands):
    """Calculate hand totals and return the results in a dictionary."""
    results = {}
    for key, value in player_hands.items():
        points = 0
        for card in value:
            if card[0] == 8:
                points += 50
            elif card[0] in ("Jack", "Queen", "King"):
                points += 10
            elif card[0] == "Ace":
                points += 1
            else:
                points += card[0]
        results[key] = points
    return results


class TestCrazyEights(unittest.TestCase):

    def test_deck(self):
        self.assertEqual(len(card_deck()), 52)

    def test_calculate_points(self):
        player_hands = {"computer": [(8, "Spades"), ("Jack", "Diamonds"), ("Ace", "Hearts"), (7, "Clubs")]}
        results = calculate_points(player_hands)
        self.assertEqual(results["computer"], 68)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCrazyEights)
unittest.TextTestRunner(verbosity=2).run(suite)
