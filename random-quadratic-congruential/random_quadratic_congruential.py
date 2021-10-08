class RandomQuadraticCongruential:
    """
    Quadratic congruent random number generator

    Y_n+1 = (ay_n^2 + by_n + c) mod m

    Parameters
    ----------
    y0 : Int
        first element of pseudorandom sequence
    m : Int
        modulus
    a: Int, optional
        first multiplier
    b: Int, optional
        second multiplier
    c: Int, optional
        increment

    Example
    ----------
    >>> from random_quadratic_congruential import RandomQuadraticCongruential
    >>> RandomQuadraticCongruential(512, 1024).sample(10)
    [0.5, 0.4990234375, 0.494140625, 0.4111328125, 0.05859375, 0.1435546875, 0.224609375, 0.3525390625, 0.5234375, 0.4443359375, 0.986328125]

    Note
    ----------
    Using m = 2^q greater than the length of the desired random sequence,
    gives the best results :

        If m = 2^q, cshould be odd
        If m = 2^q, b = (a+1) mod 4
        If m = 2^q, b - it should be odd
        If m = 2^q, a - should be even

    If m is a multiple of 9, either a mod 9 = 0, or a mod 9 = 1 and ac mod 9 = 6

    References
    ----------
    1. Linear congruential generator en.wikipedia.org. Available at: https://en.wikipedia.org/wiki/Linear_congruential_generator.


    """

    def __init__(self, y0, m, a=None, b=None, c=None):
        self.y0 = y0
        self.m = m

        if not a or not b or not c:
            a = m-2
            b = (a+1) % 4
            c = m-1

        self.a = a
        self.b = b
        self.c = c

    def is_power_two(self, x):
        """
        Check if the number is a power of two
        """
        return x & x - 1 == 0

    def sample(self, size):
        """
        Draw samples

        Parameters
        ----------
        size : Int
            N of samples

        Returns
        -------
        Y : List[Float]
            The returned samples Y[y0...yn]
        """
        Y = [self.y0]
        for _ in range(size):
            Y.append((self.a * Y[-1]**2 + self.b * Y[-1] + self.c) % self.m)

        # y = y/m, y ∈ [0, m)
        return [y / self.m for y in Y]
