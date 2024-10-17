#!/usr/bin/python3
"""
Minimum Operations to achieve n 'H' characters using Copy All and Paste operations
"""
def minOperations(n)
if n <= 1:
        return 0

    ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n = n // divisor
        divisor += 1

    return ops
