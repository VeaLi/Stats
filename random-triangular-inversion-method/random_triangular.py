import numpy as np


class RandomTriangular:
    """
    Random number generator, 
    defined by a triangular continuous distribution.

    Distribution: continuous triangular distribution
    Method: Inverse function method CDF^-1(U) = X

    Parameters
    ----------
    minimum : Float
        [a]
    mode : Float
        [b]
    maximum: Float
        [c]

    Example
    ----------
    >>> from random_triangular import RandomTriangular
    >>> tgen = RandomTriangular(1, 3, 5)
    >>> tgen.sample(10)
    [4.227567842367436, 3.8061169676232325, 3.4928648056119225, 2.6752992502923743, 3.1115694877383087, 3.5471438298532902, 3.4052578778856324, 2.4027460384076607, 3.3043270228447694, 1.2173025061137515]

    References
    ----------
    1. Generating Samples from Probability Distributions web.mit.edu. Available at: https://web.mit.edu/urban_or_book/www/book/chapter7/7.1.3.html.
    2. Random variates from the triangular distribution math.wm.edu.


    """

    def __init__(self, minimum, mode, maximum):

        self.a = minimum
        self.b = mode
        self.c = maximum

    def _inverse_triangular_cdf(self, xu, a, b, c):
        """
        Given random number [0,1] xu (from U),
        as well as the minimum of a, mode b, and maximum of c,
        returns the value of the random variable X
        """
        # from zero to mode
        if 0 <= xu and xu < ((b - a) / (c - a)):
            return a + ((c - a) * (b - a) * xu)**0.5

        # from mode to 1
        elif ((b - a) / (c - a)) <= xu and xu <= 1:
            return c - ((c - a) * (c - b) * (1 - xu))**0.5

    def sample(self, size):
        """
        Draw samples from the triangular distribution

        Parameters
        ----------
        size : Int
            N of samples

        Returns
        -------
        X : List[Float]
            The returned samples
        """

        self.size = size

        # random numbers [0,1]
        U = np.random.uniform(low=0, high=1, size=self.size)
        X = [self._inverse_triangular_cdf(x, self.a, self.b, self.c) for x in U]

        return X
