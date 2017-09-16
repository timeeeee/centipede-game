from random import random, normalvariate
from itertools import combinations

NUM_ROUNDS = 10


def play_centipede(strategy1, strategy2):
    """
    Given two mixed strategies of length NUM_ROUNDS, simulate a single game and
    return a pair of the first and second players payoffs.
    """
    small_pot, large_pot = 1, 4
    for i in range(NUM_ROUNDS):
        # Does player 1 take the large pot?
        if random() < strategy1[i]:
            return (large_pot, small_pot)

        small_pot *= 2
        large_pot *= 2

        # Does player 2 take the large pot?
        if random() < strategy2[i]:
            return (small_pot, large_pot)

        small_pot *= 2
        large_pot *= 2

    # Neither player took the large pot and we're out of rounds
    return (0, 0)


def generate_random_strategy():
    """Return a completely random strategy"""
    return [random() for _ in range(NUM_ROUNDS)]


def clamp(x, minimum, maximum):
    return max(min(x, maximum), minimum)


def mutate(strategy, stddev):
    """
    Mutate the strategy by varying each probability based on a normal
    distribution.
    """
    return [clamp(p + normalvariate(0, stddev), 0, 1) for p in strategy]


def combine(strategy1, strategy2):
    """
    """
    return [p1 if (random() < .5) else p2
            for p1, p2, in zip(strategy1, strategy2)]


def evolve(pool1, pool2):
    """
    For pools of first and second player strategies, play them against each
    other, and generate new pools based on the most successful strategies.
    """
    scores1 = [0 for _ in pool1]
    scores2 = [0 for _ in pool2]

    for index1, strategy1 in enumerate(pool1):
        for index2, strategy2 in enumerate(pool2):
            for _ in range(10):
                score1, score2 = play_centipede(strategy1, strategy2)
                scores1[index1] += score1
                scores2[index2] += score2

    print("scores:")
    print(sorted(scores1, reverse=True))
    print(sorted(scores2, reverse=True))
    print()

    # Use the 5 strategies with the best scores, and have each pair reproduce
    best1 = [pair[1] for pair in sorted(zip(scores1, pool1), reverse=True)[:5]]
    best2 = [pair[1] for pair in sorted(zip(scores2, pool2), reverse=True)[:5]]

    new_pool1 = []
    for parent1, parent2 in combinations(best1, 2):
        new_pool1.append(mutate(combine(parent1, parent2), .1))

    new_pool2 = []
    for parent1, parent2 in combinations(best2, 2):
        new_pool2.append(mutate(combine(parent1, parent2), .1))

    return new_pool1, new_pool2


if __name__ == "__main__":
    pool1 = [generate_random_strategy() for _ in range(10)]
    pool2 = [generate_random_strategy() for _ in range(10)]

    for _ in range(10000):
        pool1, pool2 = evolve(pool1, pool2)

    print(*pool1, sep="\n")
    print(*pool2, sep="\n")
