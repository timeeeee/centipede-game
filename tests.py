from nose.tools import *

from centipede import *


def test_random_strategy():
    """Are the random strategies lists of probabilities?"""
    for _ in range(100):
        strategy = generate_random_strategy()
        for p in strategy:
            assert_greater_equal(p, 0)
            assert_less_equal(p, 1)


def test_players_never_take():
    """When neither player ever takes the pot, the payoffs are always (0, 0)"""
    zero_strategy = [0 for _ in range(NUM_ROUNDS)]
    for _ in range(10):
        scores = play_centipede(zero_strategy, zero_strategy)
        assert_tuple_equal(scores, (0, 0))


def test_take_first_turn_stategy():
    """
    When the first player always takes the large pot in the first turn, the
    payoffs are always (4, 1).
    """
    for _ in range(10):
        strategy1 = generate_random_strategy()
        strategy1[0] = 1  # player1 always takes pot on first turn

        strategy2 = generate_random_strategy()

        for _ in range(10):
            assert_tuple_equal(play_centipede(strategy1, strategy2), (4, 1))


def test_mutate():
    """Mutating a strategy should not result in ridiculous probabilities"""
    zero_strategy = [0 for _ in range(NUM_ROUNDS)]
    for _ in range(100):
        for p in mutate(zero_strategy, 5):
            assert_less_equal(p, 1)
            assert_greater_equal(p, 0)

    one_strategy = [1 for _ in range(NUM_ROUNDS)]
    for _ in range(100):
        for p in mutate(one_strategy, 5):
            assert_less_equal(p, 1)
            assert_greater_equal(p, 0)
