from pyvis.network import Network


def interactive_graph(
    G,
    CLs,
    DERs,
):
    for node in G.nodes:
        G.nodes[node]["label"] = f"{node}"
        if node in DERs:
            G.nodes[node]["color"] = "#00ff00"
        elif node in CLs:
            G.nodes[node]["color"] = "#ff0000"
        else:
            G.nodes[node]["color"] = "#ffffff"

    graph = Network(notebook=True, cdn_resources="local")

    options = {
        "physics": {
            "forceAtlas2Based": {
                "theta": 0.2,
                "gravitationalConstant": -41,
                "springLength": 40,
                "springConstant": 0.53,
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based",
        }
    }
    graph.from_nx(G)
    graph.options = options
    graph.save_graph("graph.html")
