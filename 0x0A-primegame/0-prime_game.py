#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    """Returns a list of primes up to the given limit using the Sieve of Eratosthenes"""
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

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
