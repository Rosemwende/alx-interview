#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Write a method that determines if all boxes can be opened.
    """

    unlocked_boxes = {0}
    stack = {0}

    while stack:
        key = stack.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            stack.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)
