import numpy as np


class RandomByApproximation:
    """
    Randon sampling from normal distribution using method of approximations.

    Parameters
    ----------
    k : Int
        Depth of approximation, higher k closer result to the real
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
    """

    def __init__(self, k=12, mean=0, std=1):
        self.k = k
        self.mean = mean  # mu
        self.std = std  # sigma

    def _get_approximation(self):
        """
        This is an approximation for the normal distribution [1].

        Since the mean for k random numbers from U is approximately k/2 
        and the standard deviation is approximately sqrt(k/12), 
        we can transform any random number Z (obtained as the sum of k random numbers from U) 
        into a normal distribution [0,1] by subtracting the mean - k/2 and dividing by std - sqrt(k/12) 
        and then scaling to the desired distribution 
        using the desired std and centering it around the desired mean using the defined mean.
        """
        Z = np.sum(np.random.uniform(size=self.k))
        x = self.std * ((Z - (self.k / 2)) / ((self.k / 12)**0.5)) + self.mean

        return x

    def sample(self, size):
        """
        Draw samples from the distribution X

        Parameters
        ----------
        size : Int
            N of samples
        Returns
        -------
        X : List[Float]
            The returned samples
        """
        X = [self._get_approximation() for _ in range(size)]
        return X
