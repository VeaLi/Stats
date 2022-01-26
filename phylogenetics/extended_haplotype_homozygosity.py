from collections import Counter


def ehh(allseqs):
    """
    Calculates the EHH (extended haplotype homozygosity) metric for the aligned sequences, 
    it is given that the main SNP is at position 0

    Parameters
    ----------
    allseqs : List[Str]
        List of sequences for a specific allele

    Returns
    -------
    EHHs : List[Float]
        EHH metric for step plot
    """
    EHHs = []
    nas = len(allseqs)
    fnas = 1 / (nas * (nas - 1))
    for t in range(2, len(allseqs[0])+1):
        st_set = Counter([seq[0:t] for seq in allseqs])
        EHHs.append(fnas * sum([v * (v - 1) for v in st_set.values()]))

    return EHHs