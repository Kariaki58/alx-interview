#!/usr/bin/python3
"""
draw pascal triangle
"""

def factoral(n):
    """find factorial of a number"""
    if n == -1:
        return 0
    if n == 0:
        return 1
    return n * factoral(n - 1)

def find_number(n, m):
    """find the number at the nth row and mth column"""
    n_num = n - 1
    m_num = m - 1

    n_com_fac = factoral(n_num)
    m_com_fac = factoral(m_num)
    m_com_other_fac = factoral(m)

    hope_not_zero = (m_com_fac * factoral(n_num - m_num))

    if n == 0 and m == 0:
        return 1
    if hope_not_zero:
        main_comb_num = int(n_com_fac / hope_not_zero)
    else:
        main_comb_num = 0
    if n_num - m < 0:
        m_com_other_fac_num = 0
    else:
        m_com_other_fac_num = int(n_com_fac / (m_com_other_fac * factoral(n_num - m)))
    return m_com_other_fac_num + main_comb_num


def pascal_triangle(n):
    """return the diagram"""
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        triangle.append([find_number(i, j) for j in range(i + 1)])
    return (triangle)
