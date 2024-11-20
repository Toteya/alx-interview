#!/usr/bin/python3
"""
module rotate_2d_matrix: 2D Matrix manipulation
"""


def rotate_2d_matrix(matrix):
    """ Rotates the given 2D matrix clockwise by 90 degrees
    """
    r_matrix = [x[:] for x in matrix]
    for i in range(len(r_matrix)):
        for j in range(len(matrix[i])):
            matrix[j][-i - 1] = r_matrix[i][j]
