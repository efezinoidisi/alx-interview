#!/usr/bin/python3
"""
This module contains the minOperations function-
"""
import math


def get_prime_factors(n):
    """get prime factors of a number n"""
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    return prime_factors


def minOperations(n):
    """
    Given a number n, calculates the fewest number of operations needed to
    result in exactly n H characters in the file

    Args:
       n(int) : number;

    Returns:
       an integer which is the least number of operations needed.
    """
    sum = 0
    if n < 2:
        return sum
    factors = get_prime_factors(n)
    for i in range(len(factors)):
        sum += factors[i]
    return sum
