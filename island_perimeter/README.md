# Island Perimeter

This project contains a function that computes the perimeter of an island described in a grid.

## Requirements

- Ubuntu 14.04 LTS
- Python 3 (version 3.4.3)
- Code follows `PEP 8` style (version 1.7)
- No modules are imported
- All modules and functions are documented
- All files start with `#!/usr/bin/python3` and are executable

## Files

| File | Description |
|------|-------------|
| `0-island_perimeter.py` | Function `island_perimeter(grid)` that returns the perimeter of the island described in `grid` |

## Grid description

- `grid` is a list of lists of integers
- `0` represents water, `1` represents land
- Each cell is a square with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, width and height do not exceed 100
- The grid is completely surrounded by water
- There is only one island (or nothing), with no lakes

## Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

$ ./0-main.py
12
```

## Algorithm

Each land cell adds 4 to the perimeter. Every time two land cells are adjacent, they share one side, which removes 2 from the perimeter (one side from each cell).

To count each adjacent pair only once, every land cell only checks its **top** and **left** neighbors:

```
perimeter = (land cells x 4) - (adjacent pairs x 2)
```

- Time complexity: `O(rows x cols)`
- Space complexity: `O(1)`

## Author

Khaled Al-Yahya
