#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of lists): A list of lists where each sublist represents keys in a box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    unlocked_boxes = set([0])
    stack = list(boxes[0])

    while stack:
        key = stack.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            stack.extend(boxes[key])
     return len(unlocked_boxes) == len(boxes)
