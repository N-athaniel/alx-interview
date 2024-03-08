#!/usr/bin/python3
""" a function that returns a lits of lists
of integers representing the Pascal's triangle of n """


def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    
    triangle = []  # Initialize an empty list to store the triangle
    
    for i in range(n):
        row = []  # Initialize an empty list for each row
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # First and last elements are always 1
            else:
                # Calculate the value using the binomial coefficient formula
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)  # Add the row to the triangle
    
    return triangle
