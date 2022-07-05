import user_interface
import graph_functions
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    graph = graph_functions.Graph()
    
    # Homepage
    user_interface.homepage()
    plt.title("DEFAULT GRAPH")
    graph.print_graph()
    
    start = True
    while start:
        # Prompt user to select a function
        func = user_interface.user_input()

        while func:
            if func == 1:
                graph.function_one()
                break
            elif func == 2:
                graph.function_two()      
                break
            # other functions later laa when everything compile tgt
            elif func == 5:
                graph.add_new_edge()
                break
    

    # Printing the adjacency list for the graph
    # graph.print_adjacency_list()1
    