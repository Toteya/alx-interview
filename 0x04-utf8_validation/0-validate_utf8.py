#!/usr/bin/python3
"""
0-validate_utf8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Checks if the given data is a valid UTF-8 encoding
    """
    skip_iter = set()
    for i in range(len(data)):
        if i in skip_iter:
            continue

        num1 = data[i] & 0xFF
        if num1 >> 7 == 0x00:
            continue

        if num1 >> 5 == 0x06:
            try:
                num2 = data[i + 1] & 0xFF
                if num2 >> 6 == 0x02:
                    skip_iter.add(i + 1)
                    continue
                else:
                    return False
            except IndexError:
                return False
        if num1 >> 4 == 0x0E:
            try:
                num2 = data[i + 1] & 0xFF
                num3 = data[i + 2] & 0XFF
                if num2 >> 6 == 0x02 and num3 >> 6 == 0x02:
                    skip_iter.add(i + 1)
                    skip_iter.add(i + 2)
                    continue
                else:
                    return False
            except IndexError:
                return False
        if num1 >> 3 == 0x1E:
            try:
                num2 = data[i + 1] & 0xFF
                num3 = data[i + 2] & 0XFF
                num4 = data[i + 3] & 0XFF
                if num2 >> 6 == 2 and num3 >> 6 == 2 and num4 >> 6 == 2:
                    skip_iter.add(i + 1)
                    skip_iter.add(i + 2)
                    skip_iter.add(i + 3)
                    continue
                else:
                    return False
            except IndexError:
                return False
        return False
    return True
