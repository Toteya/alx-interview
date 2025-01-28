#!/usr/bin/python3
"""
Sieve of Eratosthenes:
Algorithm for finding all prime numbers below a given number n.
"""
import sys


def sieve_of_eratosthenes(n):
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


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            exit('NUMBER must be a valid integer')
    else:
        sys.exit('USAGE: sieve_of_eratosthenes NUMBER')
    if n < 2:
        sys.exit('Enter a NUMBER bigger than 1')
    prime_numbers = sieve_of_eratosthenes()
    print(prime_numbers)
