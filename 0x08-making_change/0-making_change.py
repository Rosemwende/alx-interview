#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total
"""

from collections import deque


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
        coins (list): List of the values of the coins in your possession
        total (int): The target amount to achieve with coins

    Returns:
        int: Fewest number of coins needed to meet the total, or -1 if
             the total cannot be met by any combination of coins
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        current_sum, num_coins = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum == total:
                return num_coins + 1

            if next_sum < total and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, num_coins + 1))

    return -1
