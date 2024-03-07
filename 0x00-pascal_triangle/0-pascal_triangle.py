#!/usr/bin/python3
"""solving pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        inner_numbers = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner_numbers.append(1)
            elif i > 0 and j > 0:
                adder = triangle[i - 1][j]
                inner_numbers.append(triangle[i - 1][j - 1] + adder)
        triangle.append(inner_numbers)
    return triangle
