#!/usr/bin/python3
"""Module that computes the minimum Copy All / Paste operations."""


def minOperations(n):
    """Return the fewest operations needed to reach exactly n H characters.

    Only Copy All and Paste are available, starting from a single H.
    Returns 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
