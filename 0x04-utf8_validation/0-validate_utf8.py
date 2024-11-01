#!/usr/bin/python3
"""
0-validate_utf8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Checks if the given data is a valid UTF-8 encoding
    """
    for num in data:
        num = num & 0xFF
        if num >> 7 == 0x00:
            continue
        if num >> 6 == 0x02:
            continue
        if num >> 5 == 0x06:
            continue
        if num >> 4 == 0x0E:
            continue
        if num >> 3 == 0x1E:
            continue
        return False
    return True
