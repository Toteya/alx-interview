#!/usr/bin/python3
"""
0-validate_utf8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Checks if the given data is a valid UTF-8 encoding
    """
    for num in data:
        if num >> 7 == 0:
            continue
        if num <= 0xDF and 0x20 ^ num >= 0xE0:
            if ((num & 0x0F) >> 6) | 0x02 == 2:
                continue
        if num <= 0xEF and 0x10 ^ num >= 0xF0:
            if ((num & 0x0F) >> 6) | 0x02 == 2:
                continue
        if num < 0xF7 and 0x08 ^ num >= 0xF8:
            if ((num & 0x0F) >> 6) | 0x02 == 2:
                continue
        return False
    return True
