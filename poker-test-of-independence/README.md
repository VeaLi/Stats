# Approximated Poker Test of independence of U(0, 1) random numbers


Treats random numbers (in bins) as hands with r different cards and compares the expected occurrence of r cards with the expected one using chi2 test.


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
