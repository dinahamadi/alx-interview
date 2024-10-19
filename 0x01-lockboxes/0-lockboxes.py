#!/usr/bin/python3
"""
This script defines a function to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
