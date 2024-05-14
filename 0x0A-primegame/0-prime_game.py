#!/usr/bin/python3
"""prime game graph theory"""

def isPrime(n):
    """is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generatePrimes(n):
    """generate primes"""
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """isWinner"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = generatePrimes(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

