#!/usr/bin/python3
""" Prime Game """

import math

def isprime(n):
    """ Return prime number """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def delete_numbers(n, nums):
    """ Remove numbers - return zero """
    return [num for num in nums if num % n != 0]

def isWinner(x, nums):
    """ Return name of player that won
    most rounds
    """
    nums.sort()
    Maria = 0
    Ben = 0
    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            change = False
            for i, n in enumerate(nums2):
                if n > 1 and isprime(n):
                    nums2 = delete_numbers(n, nums2)
                    change = True
                    turn += 1
                    break
            if not change:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"

