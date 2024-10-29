#!/usr/bin/env python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """ Checks if the given data is a valid UTF-8 encoding
    """
    for num in data:
        print(bin(num), end=', ')
        if num < 0xFF and 0x80 & num == 0:
            continue
        if num <= 0xCF and 0x20 ^ num >= 0xE0:
            if (num >> 6) | 0x02 == 2:
                continue
        if num <= 0xEF and 0x10 ^ num >= 0xF0:
            if (num >> 6) | 0x02 == 2:
                continue
        if num < 0xF7 and 0x08 ^ num >= 0xF8:
            if (num >> 6) | 0x02 == 2:
                continue
        return False
    return True
