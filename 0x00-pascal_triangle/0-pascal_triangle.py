#!/usr/bin/python3
"""
Pascal's Triangle generator function.

This function generates Pascal's Triangle up to the nth row.

Arguments:
    n (int): The number of rows of Pascal's Triangle.

Returns:
    list: A list of lists, each containing the elements of a row of Pascal's Triangle.
          Returns an empty list if n <= 0.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, len(triangle[i - 1])):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
