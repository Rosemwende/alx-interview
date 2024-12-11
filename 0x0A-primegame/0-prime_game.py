#!/usr/bin/python3
    """Returns a list of primes up to the given limit using the Sieve of Eratosthenes"""


def isWinner(x, nums):
    """Determines who wins the most rounds based on the prime game rules"""
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
