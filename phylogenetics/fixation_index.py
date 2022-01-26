def fixation_index(p=None):
    """
    The FST index value of 1 represents complete isolation of the subgroups, 
    while the value 0 means complete overlap.

    Parameters
    ----------
    p : List[Float]
        p allele frequencies of each population

    Returns
    -------
    fst: Float
        Fixation index
    """
    p = np.array(p)
    q = 1 - p
    Aa = 2 * p * q
    hs = np.mean(Aa)
    ht = 2 * np.mean(p) * np.mean(q)

    fst = (ht - hs) / ht

    return fs