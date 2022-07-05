from re import I
import networkx as nx
import matplotlib.pyplot as plt

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
            (vertex_list[0]["label"], vertex_list[1]["label"], distance_LA_BL),
            (vertex_list[1]["label"], vertex_list[2]["label"], distance_BL_SB),
            (vertex_list[2]["label"], vertex_list[3]["label"], distance_SB_RM),
            (vertex_list[3]["label"], vertex_list[4]["label"], distance_RM_MV),
            (vertex_list[4]["label"], vertex_list[0]["label"], distance_MV_LA)
        ])

    def print_graph(self):
        # subax1 = plt.subplot(121)
        pos=nx.get_node_attributes(self.graph, "pos")
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()
        # subax2 = plt.subplot(122)
        # nx.draw(self.graph, nlist=[range])

    """
    Resources:
    https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.edge_subgraph.html#networkx.DiGraph.edge_subgraph
    https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.nodes.html
    https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw.html
    https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
    https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
    """
    # Check shortest path
    def shortest_path(self, initial, end):
        # self.graph is the graph
        # initial is the starting vertex
        # end is the targeted vertex
            
        # If no path between both vetices
        while(not nx.has_path(self.graph, initial, end)):
            print("No path found between both vertices")
            return 0
            #print("Reenter new vertices")
            # Prompt the user to enter again

        while(initial == end):
            print("You have reach your destination")
            # Exit the program
            return 0

        # List to store the vertices of the shortest path between initial and end
        shortest_path_vertices = nx.shortest_path(self.graph, initial, end)

        # List to store the edges of the shortest path between initial and end
        shortest_path_edges = []
        for j in range(len(shortest_path_vertices)-1):
            shortest_path_edges.append((shortest_path_vertices[j],shortest_path_vertices[j+1]))
        
        # Stores the subgraph containing the shortest path traversed from desired source and target
        shortest_sub = self.graph.edge_subgraph(shortest_path_edges)
        self.print_graph(shortest_sub)
        #return shortest_sub  
    
# User interface for the user
def menu():
    print(
        """
        _________________________________________
                       FUNCTIONS
        _________________________________________
        Choose to perform:
        1: Check whether the graph is strongly connected
        2: Check whether the graph has any cycle
        3: Check the shortest path between 2 vertices
        4: Check the Minimum Spanning Tree (MST)
        5: Reset Graph
        6: Remove Edges
        7: Exit
        """
        )

def userinput():
    while True:
        try:
            choice = int(input("Choice: "))
        except ValueError:
                print("This is invalid choice. Try again!")
        else:
            return choice

def main():
    graph = Graph()
    
    running = True
    
    while running:
        menu()
        choice = userinput()
        
        while choice:
            if choice == 3:
                print("===========================================================")
                print("| Function 3:  Check the shortest path between 2 vertices |")
                print("===========================================================")
                
                print("Which path would you like to find?")
                initial = input("From: ")
                end = input("To: ")
                
                if initial not in list(graph.graph.nodes) and end not in list(graph.graph.nodes):
                    print("Invalid input. Please enter valid locations only.")
                    return 0
                    
                s_path = graph.shortest_path(initial, end)
                #graph.print_graph(s_path)
                #plt.pause(0.1)
            break
        break