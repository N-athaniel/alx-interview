#!/usr/bin/python3
''' module for working with lockboxes.
'''


def canUnlockAll(boxes):
    # Initialize a set to keep track of the boxes we can access.
    accessible_boxes = {0}  # Start with the first box (index 0).

    # Initialize a queue for BFS traversal.
    queue = [0]

    # Perform BFS to explore all reachable boxes.
    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]  # Get the keys in the current box.

        for key in keys:
            if key not in accessible_boxes:
                # If the key opens a new box, add it to the accessible set and queue.
                accessible_boxes.add(key)
                queue.append(key)

    # Check if all boxes are accessible.
    return len(accessible_boxes) == len(boxes)
