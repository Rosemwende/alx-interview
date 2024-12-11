def sieve_of_eratosthenes(limit):
    """Generate a list indicating if numbers are prime up to limit"""
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def count_primes_up_to(prime_sieve):
    """Precompute the number of primes up to each index"""
    prime_count = [0] * len(prime_sieve)
    count = 0
    for i in range(len(prime_sieve)):
        if prime_sieve[i]:
            count += 1
        prime_count[i] = count
    return prime_count

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_sieve = sieve_of_eratosthenes(max_n)
    prime_count = count_primes_up_to(prime_sieve)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
