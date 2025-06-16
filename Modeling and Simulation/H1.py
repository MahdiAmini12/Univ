import matplotlib.pyplot as plt # type: ignore
import networkx as nx 

# Create a directed graph for the state chart
G = nx.DiGraph()

# Define states
states = {
    "Off": "off",
    "On-White": "on-whitelight",
    "On-Blue": "on-bluelight"
}

# Add states and transitions
G.add_edge("Off", "On-White", label="k1 : on")
G.add_edge("On-White", "Off", label="k2 : off")
G.add_edge("On-White", "On-Blue", label="k2 : change to blue")
G.add_edge("On-Blue", "On-White", label="k2 : change to white")
G.add_edge("On-Blue", "Off", label="k1 : off")

# Layout for the graph
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=3000, edgecolors="black")

# Draw edges
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray")

# Draw labels for states
nx.draw_networkx_labels(G, pos, labels=states, font_size=10, font_color="black")

# Draw labels for transitions
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="red")

# Display the graph
plt.title("State Chart for Lamp and Switch System", fontsize=12)
plt.axis("off")
plt.show()