import graph_functions

distance_LA_BL = 9310
distance_BL_SB = 526
distance_SB_RM = 659
distance_RM_MV = 11032
distance_MV_LA = 10020

if __name__ == "__main__":
    graph = graph_functions.Graph(5)
    graph.add_edges(0, 1, distance_LA_BL)
    graph.add_edges(1, 2, distance_BL_SB)
    graph.add_edges(2, 3, distance_SB_RM)
    graph.add_edges(3, 4, distance_RM_MV)
    graph.add_edges(4, 0, distance_MV_LA)

    graph.print_matrix()