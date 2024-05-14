#!/usr/bin/python3
"""Prime Game"""

def Prime(n):
    """isPrime"""
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    return primes

def isWinner(x, nums):
    """is winner"""
    player1 = 0
    player2 = 0
    if x < 1 or not nums:
        return None 
    n = max(nums)
    primes = Prime(n)
    for idx1, is_prime in enumerate(primes, 1):
        if idx1 == 1 or not is_prime:
            continue
        for idx2 in range(idx1 + idx1, n + 1, idx1):
            primes[idx2 - 1] = False
    for _, n in zip(range(x), nums):
        p_count = len(list(filter(lambda y: y, primes[0: n])))
        player2 += p_count % 2 == 0
        player1 += p_count % 2 == 1
    if player1 == player2:
        return None
    if player1 > player2:
        return "Maria"
    else:
        return "Ben"
