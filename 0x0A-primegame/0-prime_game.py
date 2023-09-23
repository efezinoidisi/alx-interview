#!/usr/bin/python3
"""
This module contains my solution to prime_game problem
"""


def isWinner(x, nums):
    """
    returns the winner of the game played by maria and ben

    parameters:
       x - number of rounds of game
       nums - array of numbers n

    return:
      name of player that won the most rounds
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(num):
    """check if a given number is a prime number"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_round(n):
    """single game round"""
    maria_turn = True
    while n > 0:
        prime_found = False
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                prime_found = True
                n -= i
                break
        if not prime_found:
            break
        maria_turn = not maria_turn
    return "Maria" if maria_turn else "Ben"
