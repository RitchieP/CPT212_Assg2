from re import I
import networkx as nx
import matplotlib.pyplot as plt
import random

# A global list of vertex to be used in the class
# vertex_list = ["LA", "BL", "SB", "RM", "MV"]
import networkx.exception

vertex_list = [
    {"label": "LA", "fullname": "Los Angeles", "pos": (1, 4)},
    {"label": "BL", "fullname": "Berlin", "pos": (5, 6)},
    {"label": "SB", "fullname": "Salzburg", "pos": (6, 5)},
    {"label": "RM", "fullname": "Rome", "pos": (5, 3)},
    {"label": "MV", "fullname": "Montevideo", "pos": (2, 1)},
]


class Graph:
    # Constructor to initialize the graph
    def __init__(self):
        distance_BL_LA = 9310
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
    def reset_graph(self, print_graph=False):
        self.__init__()

        if print_graph:
            self.print_graph()
        
    # Add new edge enter by user
    def add_new_edge(self, v1, v2):
        self.graph.add_edge(v1, v2)
        plt.title("GRAPH WITH NEWLY ADDED EDGE")
        self.print_graph()
        
    # Add new edge enter by user
    def remove_edge(self, v1, v2):
        try:
            self.graph.remove_edge(v1, v2)
            plt.title("GRAPH WITH REMOVED EDGE")
            self.print_graph()
        except networkx.exception.NetworkXError:
            print("This edge does not exist. It could be because this edge is not in the graph"
                  "\nOR"
                  "\nThe direction of the edge is wrong")

    '''
    Function to print the graph
    If there is no graph or subgraph provided, the program will print the graph available inside the Graph class
    else, it will print the graph or subgraph provided
    '''
    def print_graph(self, selected_graph=None):
        if selected_graph is None:
            pos = nx.get_node_attributes(self.graph, "pos")
            labels = nx.get_edge_attributes(self.graph, "weight")
            nx.draw(self.graph, pos, with_labels=True, font_weight='bold', connectionstyle="arc3,rad=0.3")
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels, font_size=7)
        else:
            pos = nx.get_node_attributes(selected_graph, "pos")
            labels = nx.get_edge_attributes(selected_graph, "weight")
            nx.draw(selected_graph, pos, with_labels=True, font_weight='bold', connectionstyle="arc3,rad=0.3")
            nx.draw_networkx_edge_labels(selected_graph, pos, edge_labels=labels, font_size=7)
        plt.show()

    # Print the adjacency list of the graph
    def print_adjacency_list(self):
        print("==================================")
        print("Adjacency List for graph, first column is the starting vertex, while the following columns are adjacent "
              "vertices")
        for line in nx.generate_adjlist(self.graph):
            print(line)

    # Check if the graph has a cycle, return True if a cycle is detected
    def has_cycle(self):
        return len(sorted(nx.simple_cycles(self.graph))) > 0

    # Add a random edge in the graph
    def add_random_edge(self):
        # Define the other edge's distance
        distance_LA_SB = 9704
        distance_LA_RM = 10190
        distance_BL_RM = 1184
        distance_BL_MV = 11817
        distance_SB_MV = 11477
        distance_LA_BL = 9310
        distance_SB_BL = 526
        distance_RM_SB = 659
        distance_MV_RM = 11032
        distance_LA_MV = 10020
        
        edge_distance = 0
        # Get the list of nodes that dose not have an edge, then randomly choose from there
        nonedges = list(nx.non_edges(self.graph))
        
        # Logging
        print("\nList of edges: " + str(nonedges))
        print("Number of non-edges: " + str(len(nonedges)))

        # Compute the edge distance based on the vertex combination
        chosen_edge = list(random.choice(nonedges))
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
        elif chosen_edge[0] == "LA" and chosen_edge[1] == "BL":
            edge_distance = distance_BL_LA
        elif chosen_edge[0] == "SB" and chosen_edge[1] == "BL":
            edge_distance = distance_SB_BL
        elif chosen_edge[0] == "RM" and chosen_edge[1] == "SB":
            edge_distance = distance_RM_SB
        elif chosen_edge[0] == "MV" and chosen_edge[1] == "RM":
            edge_distance = distance_MV_RM
        elif chosen_edge[0] == "LA" and chosen_edge[1] == "MV":
            edge_distance = distance_LA_MV

        # Logging
        print("Chosen edge is between: " + chosen_edge[0] + " " + chosen_edge[1])
        print("Distance: " + str(edge_distance))

        '''
        Because of the edges generated is from an undirected graph, the direction will always be the same. The only
        random choice made is just the choice of edge. The code statements below will randomly select the starting edge
        and the ending edge randomly to produce a random direction.
        '''
        start_vertex = random.choice(chosen_edge)
        chosen_edge.remove(start_vertex)
        end_vertex = chosen_edge[0]

        # Logging
        print("Starting vertex: " + start_vertex)
        print("End vertex: " + end_vertex)

        # Add the random edge
        self.graph.add_weighted_edges_from([
            (start_vertex, end_vertex, edge_distance)
        ])

        return [start_vertex, end_vertex]
    
    # Display list of available edges to ease user to select
    def available_edges(self):
        return list(nx.non_edges(self.graph))
    
    # Display list of removable edges to ease user to select which to remove
    def removeable_edges(self):
        return list(nx.edges(self.graph))
    
    #Restriction for edge selection
    def edge_input_validation(self, start_vertex, end_vertex):
        if (start_vertex, end_vertex) in self.graph.edges:
            print("Edge already exists! Try another one.")
            return False
        elif (start_vertex, end_vertex) not in self.available_edges():
            print("Invalid Edge! Try another one.")
            return False
        else:
            return True

    def function_one(self):
        # Determine if the graph is strongly connected by using the networkx built-in function is_strongly_connected
        # This function returns True is it is a strongly connected graph
        print("\nStrongly Connected Graph: " + str(nx.is_strongly_connected(self.graph)))
        input("\nPress any key to continue...")
        
        # Generate random edge until a strongly connected graph is found
        while not nx.is_strongly_connected(self.graph):
            self.add_random_edge()
            
        # Print the graph after a strongly connected graph is found
        print("\nStrongly Connected Graph: " + str(nx.is_strongly_connected(self.graph)))
        plt.title("STRONGLY CONNECTED GRAPH")
        self.print_graph()

    def function_two(self):
        # Logging
        print("Graph cycle: " + str(self.has_cycle()))

        while not self.has_cycle():
            self.add_random_edge()
        cycle_path = sorted(nx.simple_cycles(self.graph))[0]
        print("The cycle within the graph is from: " + str(cycle_path))

        cycle_graph_vertices = []
        for j in range(len(cycle_path)):
            cycle_graph_vertices.append((cycle_path[j], cycle_path[j % len(cycle_path)]))
        subgraph = self.graph.subgraph(cycle_path)
        self.print_graph(selected_graph=subgraph)

    # Check shortest path
    def function_three(self, start_vertex, end_vertex):
        # If the vertex given is not inside the graph, abort the function
        if start_vertex not in list(self.graph.nodes) and end_vertex not in list(self.graph.nodes):
            print("Invalid input. Please enter valid locations only.")
            return

        # If no path between both vertices
        while not nx.has_path(self.graph, start_vertex, end_vertex):
            # Logging
            print("No path found between both vertices")
            self.add_random_edge()

        if len(nx.shortest_path(self.graph, start_vertex, end_vertex)) > 0:
            # Stores a subgraph generated from adding a random edge
            subgraph = self.graph.subgraph(nx.shortest_path(self.graph, start_vertex, end_vertex))
            self.print_graph(selected_graph=subgraph)
            plt.pause(0.1)
        else:
            print("Random edges added did not produce a path between the selected vertex.")
            
    def function_four(self,start_vertex, end_vertex):
        user_edge = [(start_vertex, end_vertex)] #User choice not done yet (Do it in main, pass variable after self)
        
        while True:
          G =  nx.restricted_view(self.graph,[],[i for i in list(self.graph.edges) if i not in user_edge])
          try:
              if (nx.minimum_spanning_arborescence(G)):
                  mst = nx.minimum_spanning_arborescence(G)
                  break
          except nx.exception.NetworkXException:
              if len(list(nx.non_edges(G))) > 0:
                  random_x = random.choice(list(nx.non_edges(G)))
                  user_edge.append(random_x)
              else:
                  break      
        return mst
