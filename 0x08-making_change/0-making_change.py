#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
        coins (list): List of the values of the coins in your possession
        total (int): The target amount to achieve with coins

    Returns:
              Fewest number of coins needed to meet the total
             -1 if the total cannot be met by any combination of coins
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for coin in coins:
            if t >= coin:
                dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
