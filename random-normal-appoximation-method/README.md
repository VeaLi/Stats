# Method of approximations

Random sampling from normal distribution using method of approximations.

Parameters
----------
k : Int
    Depth of approximation, higher k closer result to the true distribution
mean : Float
    Mean (mu) - center of Normal distribution
std: Float
    Standard Deviation (sigma) - spread of Normal distribution

    Example
    ----------
    >>> from random_by_approximation import RandomByApproximation
    >>> rba = RandomByApproximation(12, 4, 8)
    >>> rba.sample(10)
    [-2.55521977, 16.08215166, 10.91286278,  6.54760184,  4.04907002,
    -4.30730402,  8.62185616,  2.74680966, -2.47990582,  2.60756277]
    >>> X = rba.sample(10000)
    >>> np.mean(X);np.std(X)
    3.940207232096505
    7.952339326215744

References
----------
1. 7.1.3 Generating Samples from Probability Distributions web.mit.edu. Available at: https://web.mit.edu/urban_or_book/www/book/chapter7/7.1.3.html.
