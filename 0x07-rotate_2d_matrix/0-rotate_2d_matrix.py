#!/usr/bin/python3
"""
Rotate 2D Matrix 90 Degrees Clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place

    Args:
        matrix (list[list[int]]): The n x n 2D matrix to rotate
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
