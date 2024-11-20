#!/usr/bin/python3
"""
This function generates Pascal's Triangle up to the nth row

Arguments:
    n (int): The number of rows of Pascal's Triangle

Returns:
    A list of lists, each containing the elements of a row of Pascal's Triangle
          Returns an empty list if n <= 0
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
