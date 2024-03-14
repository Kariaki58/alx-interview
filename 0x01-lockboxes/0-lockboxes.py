#!/usr/bin/python3
"""lockboxes"""

def canUnlockAll(boxes):
    """unlock a box"""
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
