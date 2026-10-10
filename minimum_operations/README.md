# Minimum Operations

Given a file with a single `H` character and only two operations,
`Copy All` and `Paste`, `minOperations(n)` returns the fewest operations
needed to reach exactly `n` `H` characters, or `0` if impossible.

## Approach

Copying `k` characters and pasting `m - 1` times multiplies the count
by `m` at a cost of `m` operations. The minimum is therefore the sum of
the prime factors of `n`.

## File

- `0-minoperations.py`: `minOperations(n)`

## Author

Khaled Al-Yahya
