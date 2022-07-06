import graph_functions

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
        6: Add New Edges
        7: Remove Edges
        8: Exit
        """
        )


def user_input():
    choice = int(input("Choice: "))
    try:
        while choice < 1 or choice > 8:
            print("This is invalid choice. Try again!")
            choice = int(input("Choice: "))
    except ValueError:
        print("This is invalid choice. Try again!")
    return choice


def function_interface(choice, graph):
    if choice == 1:
        print("======================================================")
        print("| Function 1:  Check whether the graph is strongly connected |")
        print("======================================================")
        graph.function_one()
    
    elif choice == 2:
        print("======================================================")
        print("| Function 2:  Check whether the graph has any cycle |")
        print("======================================================")
        graph.function_two()
    
    elif choice == 3:
        print("===========================================================")
        print("| Function 3:  Check the shortest path between 2 vertices |")
        print("===========================================================")

        print("\nWhich path would you like to find?")
        print("\nEnter any one of the city abbreviation as follow" +
              "\n[LA / BL / SB / RM / MV]")
        start_vertex = input("From: ")
        end_vertex = input("To: ")
        graph.function_three(graph, start_vertex, end_vertex)
    
    elif choice == 4:
        pass
    
    elif choice == 5:
        print_graph = str(input("Print graph after reset? [y/n]")).lower()
        if print_graph == 'y':
            graph.reset_graph()
            graph.print_graph()
        else:
            graph.reset_graph()
    
    elif choice == 6:
        print("\nWhich edge would you like to add?")
        print("\nEnter any one of the city abbreviation as follow" +
        "\n[LA / BL / SB / RM / MV]")
        start_vertex = input("From: ")
        end_vertex = input("To: ")
        graph.add_new_edge(start_vertex, end_vertex)
    
    elif choice == 7:
        print("\nWhich edge would you like to remove?")
        print("\nEnter any one of the city abbreviation as follow" +
        "\n[LA / BL / SB / RM / MV]")
        start_vertex = input("From: ")
        end_vertex = input("To: ")
        graph.remove_edge(start_vertex, end_vertex)
    
    else:
        print("Something went wrong when taking user input, you have an input error. Try making an input again.")
        return