# Lockboxes

## Description
This project solves the **Lockboxes** problem: given `n` locked boxes numbered `0` to `n - 1`, where each box may contain keys to other boxes, determine whether all boxes can be unlocked starting from box `0` (which is always unlocked).

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- First line of all files is exactly `#!/usr/bin/python3`
- Code follows the `PEP 8` style (version 1.7.x)
- All files are executable

## Files

| File | Description |
|---|---|
| `0-lockboxes.py` | Contains `canUnlockAll(boxes)`, which determines if all boxes can be opened |

## Approach
The problem is modeled as a graph traversal: each box is a node, and each key inside a box is an edge to another box.

1. Start with box `0` marked as opened (`opened = {0}`), and queue its keys for checking (`to_check`).
2. While there are keys left to check:
   - Pop a key from `to_check`.
   - If the key refers to a valid box (`key < len(boxes)`) and that box hasn't been opened yet, mark it as opened and add its keys to `to_check`.
3. After the traversal, compare the number of opened boxes to the total number of boxes. If they match, every box can be unlocked.

This is equivalent to a BFS/DFS reachability check from a starting node in a graph.

## Example

```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
# True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
# False
```

## Author
Khaled Al-Yahya
