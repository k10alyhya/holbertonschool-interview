#!/usr/bin/python3
"""Module that determines if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list): list of lists, where boxes[i] contains the
            keys needed to open other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    opened = {0}
    to_check = boxes[0]

    while to_check:
        key = to_check.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            to_check.extend(boxes[key])

    return len(opened) == len(boxes)
