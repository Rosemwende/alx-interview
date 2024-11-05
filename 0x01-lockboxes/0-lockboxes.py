#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked_boxes = set([0])
    stack = [key for key in boxes[0]]

    while stack:
        key = stack.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            stack.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)
