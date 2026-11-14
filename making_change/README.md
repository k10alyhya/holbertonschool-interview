# Making Change

Given a list of coin values, find the fewest number of coins needed to meet a given total.

## Task

| File | Description |
|------|-------------|
| `0-making_change.py` | `makeChange(coins, total)` returns the fewest coins needed to meet `total`, `0` if `total <= 0`, or `-1` if it cannot be met |

## Approach

Dynamic programming (bottom-up): `dp[x]` holds the fewest coins needed for amount `x`.
For each coin, every amount from the coin value up to `total` is updated with `dp[x - coin] + 1` if that is smaller.

- Time complexity: O(len(coins) × total)
- Space complexity: O(total)

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- PEP 8 style (version 1.7.x)

## Author

Khaled Al-Yahya
