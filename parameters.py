import networkx as nx
import numpy as np


# Returns ratio of number of critical loads to number of sources
def ratio_source_load(possible_networks, CLs, DERs):
    rsl = []
    for path in possible_networks:
        loads, sources = set(), set()
        for u, v in path:
            if u in CLs:
                loads.add(u)
            if v in CLs:
                loads.add(v)
            if u in DERs:
                sources.add(u)
            if v in DERs:
                sources.add(v)
        if len(loads) == 0:
            rsl.append(0)
            continue
        rsl.append(len(loads) / len(sources))
    return rsl


# Returns switching operations required to operate
def switch_ops(possible_networks, wt):
    ops = []
    for path in possible_networks:
        cnt = 0
        for edge in path:
            if wt[edge] == 0:
                cnt += 1
        ops.append(cnt)
    return ops


# Returns aggregated degree centrality of the network
def agg_centrality(possible_networks):
    deg_cent = []
    for path in possible_networks:
        G = nx.Graph(path)
        deg = np.average([x for x in nx.degree_centrality(G).values()])
        deg_cent.append(deg)
    return deg_cent
