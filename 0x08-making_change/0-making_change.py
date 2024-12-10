#!/usr/bin/python3
"""
a scripy that determine the fewest number of coins needed to meet the total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
