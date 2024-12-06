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
                perimeter = update_perimeter(perimeter, grid, i, j, True)
            else:
                perimeter = update_perimeter(perimeter, grid, i, j, False)
    return perimeter


def update_perimeter(perimeter, grid, i, j, on_land):
    """ Updates the perimeter depending on the given cells (coordinates)
    """
    if on_land:
        try:
            if not grid[i][j - 1]:
                perimeter += 1
        except IndexError:
            perimeter += 1
        try:
            if not grid[i - 1][j]:
                perimeter += 1
        except IndexError:
            perimeter += 1

    else:
        try:
            if grid[i][j - 1]:
                perimeter += 1
        except IndexError:
            pass
        try:
            if grid[i - 1][j]:
                perimeter += 1
        except IndexError:
            pass
    return perimeter
