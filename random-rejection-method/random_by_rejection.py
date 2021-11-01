import numpy as np


class RandomByRejection:
    """
    Random sampling from a distribution X by the rejection method on a uniform distribution U.
    Given the probability density function of the desired distribution X - pdf, sample random numbers from that distribution.

    Parameters
    ----------
    f : Func(x)->y
        Function that returns a random number (f() belongs to X) from U
    pdf : Func(x)->p
        Probability density function of X
    max_pdf: Float
        Maximum of a given probability density function, aka the "height" of the distribution

    Example
    ----------
    >>> from random_by_rejection import RandomByRejection
    >>> rbj = RandomByRejection(f, pdf, max_pdf)
    >>> rbj.sample(10)
    [5.960490859234767, 4.749522023202175, 3.146933717716522, 
    6.192637916602297, 8.44873270536448, 3.7206028389123578, 
    4.945114547015546, 3.040876425727124, 4.524948973535853, 5.37190297767069]

    References
    ----------
    1. Rejection sampling wikipedia. Available at: https://en.wikipedia.org/wiki/Rejection_sampling
    """

    def __init__(self, f, pdf, max_pdf):
        self.f = f
        self.pdf = pdf
        self.max_pdf = max_pdf

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
        X = []

        while len(X) < size:

            x = self.f()
            y = self.pdf(x)
            u = np.random.uniform(0, self.max_pdf)

            if u < y:
                X.append(x)

        return X
