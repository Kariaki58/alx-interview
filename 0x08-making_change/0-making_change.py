#!/usr/bin/python3
"""change comes from within"""


def makeChange(coins, total):
    """makechange function"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for data in coins:
            if i >= data:
                dp[i] = min(dp[i], dp[i - data] + 1)
            else:
                pass

    return -1 if dp[total] == float('inf') else dp[total]
