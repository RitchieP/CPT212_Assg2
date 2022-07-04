import networkx as nx
import matplotlib.pyplot as plt
import random

# A global list of vertex to be used in the class
# vertex_list = ["LA", "BL", "SB", "RM", "MV"]
vertex_list = [
    {"label": "LA", "fullname": "Los Angeles", "pos": (1, 4)},
    {"label": "BL", "fullname": "Berlin", "pos": (5, 6)},
    {"label": "SB", "fullname": "Salzburg", "pos": (5, 5)},
    {"label": "RM", "fullname": "Rome", "pos": (5, 3)},
    {"label": "MV", "fullname": "Montevideo", "pos": (2, 1)},
]


class Graph:
    # Constructor to initialize the matrix
    def __init__(self):
        distance_LA_BL = 9310
        distance_BL_SB = 526
        distance_SB_RM = 659
        distance_RM_MV = 11032
        distance_MV_LA = 10020

        self.graph = nx.DiGraph()
        self.graph.add_nodes_from([
            (vertex_list[0]["label"], {"pos": vertex_list[0]["pos"]}),
            (vertex_list[1]["label"], {"pos": vertex_list[1]["pos"]}),
            (vertex_list[2]["label"], {"pos": vertex_list[2]["pos"]}),
            (vertex_list[3]["label"], {"pos": vertex_list[3]["pos"]}),
            (vertex_list[4]["label"], {"pos": vertex_list[4]["pos"]}),
        ])

        self.graph.add_weighted_edges_from([
            (vertex_list[1]["label"], vertex_list[0]["label"], distance_LA_BL),
            (vertex_list[1]["label"], vertex_list[2]["label"], distance_BL_SB),
            (vertex_list[2]["label"], vertex_list[3]["label"], distance_SB_RM),
            (vertex_list[3]["label"], vertex_list[4]["label"], distance_RM_MV),
            (vertex_list[4]["label"], vertex_list[0]["label"], distance_MV_LA)
        ])

    # Reset the graph by reinitializing the graph
    def reset_graph(self):
        self.__init__()

    # Function to print the graph
    def print_graph(self):
        pos = nx.get_node_attributes(self.graph, "pos")
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

    # Check if the graph has a cycle, return True if a cycle is detected
    def has_cycle(self):
        if len(sorted(nx.simple_cycles(self.graph))) < 1:
            return False
        return True

    # Add a random edge in the graph
    def add_random_edge(self):
        distance_LA_SB = 9704
        distance_LA_RM = 10190
        distance_BL_RM = 1184
        distance_BL_MV = 11817
        distance_SB_MV = 11477

        edge_distance = 0
        # Get the list of nodes that dose not have an edge, then randomly choose from there
        nonedges = list(nx.non_edges(self.graph))

        # Logging
        print(nonedges)
        print("Number of non-edges: " + str(len(nonedges)))

        chosen_edge = random.choice(nonedges)
        if (chosen_edge[0] == "LA" or chosen_edge[1] == "LA") and (chosen_edge[0] == "SB" or chosen_edge[1] == "SB"):
            edge_distance = distance_LA_SB
        elif (chosen_edge[0] == "LA" or chosen_edge[1] == "LA") and (chosen_edge[0] == "RM" or chosen_edge[1] == "RM"):
            edge_distance = distance_LA_RM
        elif (chosen_edge[0] == "BL" or chosen_edge[1] == "BL") and (chosen_edge[0] == "RM" or chosen_edge[1] == "RM"):
            edge_distance = distance_BL_RM
        elif (chosen_edge[0] == "BL" or chosen_edge[1] == "BL") and (chosen_edge[0] == "MV" or chosen_edge[1] == "MV"):
            edge_distance = distance_BL_MV
        elif (chosen_edge[0] == "SB" or chosen_edge[1] == "SB") and (chosen_edge[0] == "MV" or chosen_edge[1] == "MV"):
            edge_distance = distance_SB_MV

        # Logging
        print("Chosen edge is from: " + chosen_edge[0] + " " + chosen_edge[1])
        print("Distance: " + str(edge_distance))

        # Add the random edge
        self.graph.add_weighted_edges_from([
            (chosen_edge[0], chosen_edge[1], edge_distance)
        ])

    def function_two(self):
        # Logging
        print("Graph cycle: " + str(self.has_cycle()))

        while not self.has_cycle():
            self.add_random_edge()
        self.print_graph()