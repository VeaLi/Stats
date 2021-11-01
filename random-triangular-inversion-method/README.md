# Triangular random number generator, inversion method


Draw samples from the triangular distribution.


    Example
    ----------
    >>> from random_triangular import RandomTriangular
    >>> tgen = RandomTriangular(1, 3, 5)
    >>> tgen.sample(10)
    [4.227567842367436, 3.8061169676232325, 3.4928648056119225, 2.6752992502923743, 3.1115694877383087, 3.5471438298532902, 3.4052578778856324, 2.4027460384076607, 3.3043270228447694, 1.2173025061137515]
    
References
----------
1. Generating Samples from Probability Distributions web.mit.edu. Available at: https://web.mit.edu/urban_or_book/www/book/chapter7/7.1.3.html.
2. Random variates from the triangular distribution math.wm.edu.
