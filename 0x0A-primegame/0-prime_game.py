#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """check winner"""
    def sieve(n):
        """sieve"""
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    def canWin(n):
        """can Win"""
        primes = sieve(n)
        if primes.count(True) % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = canWin(n)
        wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None

if __name__=="__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
