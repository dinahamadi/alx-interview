#!/usr/bin/python3
"""
This script defines the `minOperations` function which calculates
the fewest number of operations required to achieve exactly `n` H
characters in a text file, starting with a single 'H'.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters.
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
