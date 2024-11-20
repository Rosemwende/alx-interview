#!/usr/bin/python3
"""
Function that determines if all boxes can be unlocked
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened by unlocking them with keys
    
    Args:
       A list where each list contains the keys for the boxes
    
    Returns:
        True if all boxes can be opened, otherwise False
    """
    unlocked = set([0])
    keys = set([0])
    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key not in unlocked:
                unlocked.add(new_key)
                keys.add(new_key)
    return len(unlocked) == len(boxes)
