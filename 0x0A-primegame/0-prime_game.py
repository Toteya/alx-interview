#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """ Determines and returns the player that has won the most rounds
    """
    ben_victories = 0
    maria_victories = 0
    for num in nums:
        primes = sieve_of_eratosthenes(num)
        maria_wins = False
        for _ in range(x):
            if not primes:
                break
            primes = primes[1:]
            maria_wins = not maria_wins

        if maria_wins:
            maria_victories += 1
        else:
            ben_victories += 1

    if maria_victories > ben_victories:
        return 'Maria'
    elif ben_victories > maria_victories:
        return 'Ben'
    else:
        return None


def sieve_of_eratosthenes(n):
    """ Finds all the prime numbers below a given number n
    """
    nums = list(range(2, n + 1))

    prime_numbers = nums.copy()

    # Remove numbers that are npt prime from the prime_numbers list
    for num in nums:
        # Skip if number has already been removed from prime_numbers list
        if num not in prime_numbers:
            continue
        # Find all numbers larger or equal to n^2 that are divisible by n
        i = num * num
        while i <= n:
            # Skip if number has already been removed from prime_numbers list
            if i not in prime_numbers:
                i += 1
                continue
            if i % num == 0:
                prime_numbers.remove(i)
            i += 1

    return prime_numbers
