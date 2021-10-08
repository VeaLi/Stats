from scipy.stats import iqr
import math

def freedman_diaconis(X):
    """
    Find number of bins using Freedman–Diaconis rule:

        bin width = 2 * ( IQR(X) / (LEN(X)^(1/3)) )

    Parameters
    ----------
    X : array_like
        Random variable

    Returns
    -------
    nb : List[Float]
        number of bins
    """
    w = 2 * (iqr(X) / (len(X)**(1 / 3)))
    rng = max(X) - min(X)
    nb = int(math.ceil(rng / w))
    
    return nb
