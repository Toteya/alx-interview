#!/usr/bin/python3
"""
module 0-island_perimeter
"""


def island_perimeter(grid):
    """ Computes the perimeter of an island on the given 2d grid
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                if j == 0 or not grid[i][j - 1]:
                    perimeter += 1
                if i == 0 or not grid[i - 1][j]:
                    perimeter += 1
                if i + 1 >= len(grid):
                    perimeter += 1
                if j + 1 >= len(grid[i]):
                    perimeter += 1
            else:
                if j != 0 and grid[i][j - 1]:
                    perimeter += 1
                if i != 0 and grid[i - 1][j]:
                    perimeter += 1
    return perimeter
