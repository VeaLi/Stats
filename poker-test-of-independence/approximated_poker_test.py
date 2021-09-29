from functools import lru_cache, reduce
import operator
from scipy.stats import chisquare


class PokerRandomnessTest:
    """
    Approximated Poker Test for testing random number generators

    Parameters
    ----------
    k : Int
        Length of the group
    d : Int, default=10
        Number of bins

    Example
    ----------
    >>> pt = PokerRandomnessTest(4, 10)
    >>> pt.test(np.random.uniform(size=10000))
    observed~expected
    9~10
    609~630
    4291~4320
    5091~5040

    (1.5107473544973424, 0.6797920772484682)

    References
    ----------
    1. Abdel-Rehim, W.M.F., Ismail, I.A. and Morsy, E. (2012) ‘Testing randomness: Implementing poker approaches with  hands of four numbers’, 9(4), pp. 59–64.
    2. Stirling numbers of the second kind rosettacode.org. Available at: https://rosettacode.org/wiki/Stirling_numbers_of_the_second_kind.

    """

    def __init__(self, k, d=10):
        self.k = k
        self.d = d

        self._compute_p(k, d)

    @lru_cache
    def _get_stirling2nd(self, n, k):
        """
        Compute Stirling number of the second kind: 
        the number of ways to divide a set of n objects into k non-empty subsets
        """
        if n == k == 0:
            return 1
        if (n > 0 and k == 0) or (n == 0 and k > 0):
            return 0
        if n == k:
            return 1
        if k > n:
            return 0
        result = k * \
            self._get_stirling2nd(n - 1, k) + \
            self._get_stirling2nd(n - 1, k - 1)

        return result

    def _compute_p(self, k, d):
        """
        Compute the probability of obtaining r distinct values in the group of length k.
        Pr = (d(d-1) .. (d-r-1))/d^k * s(n,k)
        """
        self.p = {r: 0 for r in range(1, k + 1)}
        for r in range(1, k + 1):
            self.p[r] = d * reduce(operator.mul, [d - i
                                                  for i in range(1, r)], 1)
            self.p[r] /= d**k
            self.p[r] *= self._get_stirling2nd(k, r)

    def _count_all_k_series(self, X):
        """
        Compute the frequencies of r distinct numbers in the group k in the sample X
        """
        self.kseq_cnt = {r: 0 for r in range(1, self.k + 1)}

        for i in range(0, len(X)):
            kseq = X[i:i + self.k]
            kseq = [int(f * self.d) for f in kseq]
            self.kseq_cnt[len(set(kseq))] += 1

    def test(self, X):
        """
        Run test

        Parameters
        ----------
        X : array_like
            Sample of random numbers in [0,1]

        Returns
        -------
        statistics : Tuple(float, float)
            Chi2 statistic and p-value
        """
        self._count_all_k_series(X)
        N = len(X)
        expected = {k: v * N for k, v in self.p.items()}
        observed = {k: v for k, v in sorted(
            self.kseq_cnt.items(), key=lambda x: x[0])}

        print(f'observed~expected')
        for o, e in zip(observed.values(), list(expected.values())):
            print(f'{o}~{round(e)}')

        statistics = chisquare(list(observed.values()),
                               list(expected.values()))

        return tuple(statistics)
