import math


def binomial_coefficient(n, k=2):
    """
    Calculates the number of sets with k elements 
    that can be chosen from a set with n elements

    Parameters
    ----------
    n : Int
        length of fixed set of n elements
    k: Int
        length of subset
        (default: k=2) same as  n(n-1)/2

    Returns
    -------
    bcoef: Int
        Num of ways to choose an unordered subset of k elements 
        from a fixed set of n elements
    """
    tp = math.factorial(n)
    bt = math.factorial(k) * math.factorial(n - k)
    bcoef = int(tp / bt)
    return bcoef