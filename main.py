import user_interface
import graph_functions
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    graph = graph_functions.Graph()
    
    print("Default graph is as follow:")
    graph.print_graph()

    while True:
        user_interface.menu()
        choice = user_interface.user_input()
        if choice == 8:
            break
        user_interface.function_interface(choice, graph)


    # Printing the adjacency list for the graph
    # graph.print_adjacency_list()1
    