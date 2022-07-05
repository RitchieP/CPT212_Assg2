import graph_functions

if __name__ == "__main__":
    graph = graph_functions.Graph()

    # Printing the adjacency list for the graph
    graph.print_adjacency_list()
    print("Default graph is as follow:")
    graph.print_graph()

    while True:
        graph_functions.menu()
        choice = graph_functions.user_input()
        if choice == 7:
            break
        graph_functions.function_interface(choice, graph)
