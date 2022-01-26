import matplotlib.pyplot as plt
import numpy as np

def wright_fisher_simulation(p, Ne, num_replicates, num_generations):
    """
    Wright-Fisher model describes change in the frequency of an existing allele 
    in a population due to random sampling of organisms (gene drift).

    P = (ntrials, num_successes) = p_success^num_successes * p_failure^num_fails

    - closer the initial AF to 0 - higher probability of allele elimination
    - probability of allele elimination also depends on population size 
    the probability is higher if the population is smaller

    Parameters:
    -----
    p: Float
        Allele frequency
    Ne: Int
        Effective population size
    num_replicates: Int
    num_generations: Int
    """

    trials = Ne * 2

    p_finals = []
    for r in tqdm(range(num_replicates)):
        P = [p]
        for g in range(num_generations):
            p_success = P[-1]
            P.append(np.random.binomial(trials, p_success) / trials)

        p_final = P[-1]
        p_finals.append(p_final)
        plt.plot(P, linewidth=1)

    plt.show()

    return p_finals


# usage :
# num_replicates, num_generations = 1000, 300
# population = wright_fisher_simulation(0.1, 1000, num_replicates, num_generations)