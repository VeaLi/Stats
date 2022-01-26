from binomial_coefficient import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def plot_population_size(N, T):
    """
    Calculates the average population sizes (psizes) of coalescent intervals T 
    using a priori knowledge of the number of genealogical lineages in the interval provided in N.
    Using the logic of the classical skyline method.

    Shows the demographic history.

    Parameters
    ----------
    N : List[Int]
        Num of branches from tree topology 
        (the number of genealogical lineages in the interval t ∈ T)
    T : List[Int]
        Coalescence times (interval size)

    References
    -----
    Ho, S. Y., & Shapiro, B. (2011). Skyline-plot methods for 
    estimating demographic history from nucleotide sequences. Molecular ecology resources, 
    11(3), 423–434. https://doi.org/10.1111/j.1755-0998.2011.02988.x
    """
    psize = []
    for n, t in zip(N, T):
        psize.append(binomial_coefficient(n) / 2 * t)
    I = 0
    plt.step([0] + [I :=I + t for t in T], [psize[0]] + psize)
    plt.ylabel('Population size')
    plt.xlabel('Time before present')
    plt.title('Demographic history')
    plt.show()

    print(f"Population sizes: {psize}")