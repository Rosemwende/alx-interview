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
        return [i for i in range(limit + 1) if sieve[i]]

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_range = [p for p in primes if p <= n]

        if len(primes_in_range) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
