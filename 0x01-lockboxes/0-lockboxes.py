#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ CAN UNLOCK ALL BOXES """
    seen_boxes = {0}
    unseen_boxes = set(boxes[0])

    while unseen_boxes:
        box_idx = unseen_boxes.pop()
        if 0 <= box_idx < len(boxes) and box_idx not in seen_boxes:
            unseen_boxes.update(boxes[box_idx])
            seen_boxes.add(box_idx)

    return len(boxes) == len(seen_boxes)
