#!/usr/bin/python3
"""
module 0-making_change
"""

def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet the given total
    """
    if total <= 0:
        return 0
    
    coin_count = 0
    
    while len(coins) > 0:
        max_coin = max(coins)
        coins.remove(max_coin)

        if (total < max_coin):
            continue
        
        coin_count += int(total / max_coin)
        total = total % max_coin

        if total == 0:
            break

    if total > 0:
        return -1
    else:
        return  coin_count
