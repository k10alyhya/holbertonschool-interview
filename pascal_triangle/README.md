# Pascal's Triangle

## Description
This repository contains a Python implementation of **Pascal's Triangle**. It calculates and returns a list of lists of integers representing the triangle for a given integer `n`.

## Tasks

### 0. Pascal's Triangle
* **File:** `0-pascal_triangle.py`
* **Prototype:** `def pascal_triangle(n):`
* **Returns:** 
  * A list of lists of integers representing Pascal's triangle of `n`.
  * An empty list `[]` if `n <= 0`.

## Requirements
* All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.x).
* Code adheres to the `pycodestyle` (version 2.7.x) style guidelines.
* All files are executable (`chmod +x`).

## Environment
* **OS:** Ubuntu 20.04 LTS
* **Language:** Python 3.8

## Usage & Example

You can test the implementation using the provided test script `0-main.py`:

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
