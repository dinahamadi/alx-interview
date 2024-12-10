#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of each game round based on optimal play.
    """

    def find_prime(max_num):
        """Helper function to calculate prime numbers up to max_num."""
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_num ** 0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, max_num + 1, i):
                    primes[multiple] = False
        return primes

    if x < 1 or not nums:
        return None

    max_num = max(nums)
    prime_flags = find_prime(max_num)
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if prime_flags[i] else 0)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
