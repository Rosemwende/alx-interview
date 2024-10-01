def pascal_triangle(n):
    """
    Generates Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
