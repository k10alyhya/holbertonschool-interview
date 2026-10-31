# N Queens

## Description
The N queens puzzle is the challenge of placing N non-attacking queens on an N x N chessboard.
This program prints every possible solution using **backtracking**.

## Requirements
- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.*)
- Only the `sys` module is imported

## Usage
```bash
./0-nqueens.py N
```
- `N` must be an integer greater or equal to 4
- Wrong number of arguments: prints `Usage: nqueens N` and exits with status 1
- `N` not an integer: prints `N must be a number` and exits with status 1
- `N` smaller than 4: prints `N must be at least 4` and exits with status 1

## Example
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
Each pair is `[row, column]` of one queen.

## How it works
1. Place one queen per row, starting from row 0.
2. For each column in the current row, check if the queen is safe:
   - no other queen in the same column
   - no other queen on the same diagonal (`|row1 - row2| == |col1 - col2|`)
3. If it is safe, place it and move to the next row.
4. When all N rows have a queen, save the solution.
5. Remove the last queen (backtrack) and try the next column.

## Files
| File | Description |
|------|-------------|
| `0-nqueens.py` | Solves the N queens puzzle and prints every solution |

## Author
Khaled Al-Yahya
