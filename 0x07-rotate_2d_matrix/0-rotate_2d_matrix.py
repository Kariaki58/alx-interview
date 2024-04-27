#!/usr/bin/env python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """matrix rotation"""
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(length):
        matrix[i].reverse()
