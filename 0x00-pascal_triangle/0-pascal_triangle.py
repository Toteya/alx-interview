#!/usr/bin/python3
"""
module: 0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates and returns a Pascal's triangle of height in the form of a
    list of lists
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            try:
                prev_row = triangle[i - 1]
            except IndexError:
                row.append(1)
                break
            if j:
                a = prev_row[j - 1]
            else:
                a = 0
            if j < i:
                b = prev_row[j]
            else:
                b = 0
            row.append(a + b)
            
        triangle.append(row)
    
    return triangle
