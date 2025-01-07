import sys, math
"""Generalization"""

def identity(k):
    return k

def cube(k):
    return k ** 3

def fn(k):
    return 8 / ((4*k - 1) * (4*k - 3))

def summation(n: int, term) -> int:
    """Sums the first N numbers in the sequence where the nth term is given.
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers.
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the cubes of first N natural numbers.
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

def converging_pi(n):
    """
    >>> converging_pi(sys.maxsize)
    math.pi
    """
    return summation(n, fn)

