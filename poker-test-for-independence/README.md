# Approximated Poker Test of independence of U(0, 1) random numbers


Treats random numbers (in bins) as hands with r different cards and compares the expected occurrence of r cards with the expected one using chi2 test.

    Example
    ----------
    >>> from approximated_poker_test import ApproximatedPokerTest
    >>> pt = ApproximatedPokerTest(4,10)
    >>> import numpy as np
    >>> pt.test(np.random.uniform(size=10000))
    observed~expected
    8~10
    589~630
    4309~4320
    5094~5040
    (3.674834656084651, 0.29878447375220785)
    
References
----------
1. Abdel-Rehim, W.M.F., Ismail, I.A. and Morsy, E. (2012) ‘Testing randomness: Implementing poker approaches with  hands of four numbers’, 9(4), pp. 59–64.
2. Stirling numbers of the second kind rosettacode.org. Available at: https://rosettacode.org/wiki/Stirling_numbers_of_the_second_kind.
