from __future__ import division

def edge_similarity(a, b):
    """
    Defining similarity between two networks as the intersection of
    their edgelists over the union of their edgelists

    Parameters
    ----------
    a: networkx graph
    b: networkx graph

    Returns
    -------

    """
    a_edge_set = set(a.edges())
    b_edge_set = set(b.edges())
    union = a_edge_set | b_edge_set
    intersection = a_edge_set & b_edge_set
    if len(union) == 0:
        similarity = 0
    else:
        similarity = len(intersection) / len(union)
    return similarity
