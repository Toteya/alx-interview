#!/usr/bin/python3
"""
module: 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Checks if all the boxes in the list can be unlocked
    """
    key_set = {0, }
    open_boxes = set()
    set_is_full = False
    box_opened = True

    while box_opened:
        box_opened = False
        keys = key_set.copy()
        for key in keys:
            if key not in open_boxes and key in range(len(boxes)):
                key_set.update(boxes[key])
                open_boxes.add(key)
                box_opened = True

    if open_boxes == set(range(len(boxes))):
        set_is_full = True

    return set_is_full
