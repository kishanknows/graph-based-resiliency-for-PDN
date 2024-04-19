import networkx as nx
import itertools


class Utils:
    def make_graph(self, line_data):
        G = nx.Graph()
        status = {}
        for u, v, s in zip(line_data["fbus"], line_data["tbus"], line_data["status"]):
            G.add_edge(u, v)
            status[(u, v)] = s
            status[(v, u)] = s
        return G, status

    def find_path_list(self, G, CLs, DERs):
        path_list = []
        for cl in CLs:
            tmp = []
            for path in nx.all_simple_paths(G, source=cl, target=DERs):
                loads, sources = 0, 0
                for node in path:
                    if node in CLs:
                        loads += 1
                    if node in DERs:
                        sources += 1
                if loads > 1 or sources > 1:
                    continue
                tmp.append(list(nx.utils.pairwise(path)))
            if len(tmp) == 0:
                continue
            path_list.append(tmp)
        return path_list

    def path_combinations(self, path_list):
        FNs = []
        raw_combs = []
        for element in itertools.product(*path_list):
            tmp = []
            for path in element:
                for edge in path:
                    tmp.append(edge)
            raw_combs.append(list(element))
            FNs.append(tmp)
        return FNs, raw_combs
