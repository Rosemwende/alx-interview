#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines who wins the most rounds based on the prime game rules"""
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(limit):
        """Generates a list of prime numbers up to a given limit"""
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return sieve

    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)

    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = prime_counts[n]

        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
