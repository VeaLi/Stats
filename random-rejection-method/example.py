from random_by_rejection import *
import matplotlib.pyplot as plt


def triang_pdf(x, minimum, maximum, mode):
    """
    Probability density function of the triangular distribution
    """
    if x <= minimum:
        return 0
    elif minimum < x and x <= mode:
        return (2 * (x - minimum)) / ((maximum - minimum) * (mode - minimum))
    elif mode < x and x <= maximum:
        return (2 * (maximum - x)) / ((maximum - minimum) * (maximum - mode))
    elif x > maximum:
        return 0




minimum = 1
maximum = 10
mode = 5


pdf = lambda x: triang_pdf(x, minimum=minimum, maximum=maximum, mode=mode)
f = lambda: np.random.uniform(minimum, maximum)
max_pdf = pdf(mode) # mode is the highest point of the triangular distribution

print(f'pdf(mode) = {max_pdf}')

rbj = RandomByRejection(f, pdf, max_pdf)
X = rbj.sample(10000)

plt.hist(X)
plt.show()