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
        print("==============================================================")
        print("| Function 1:  Check whether the graph is strongly connected |")
        print("==============================================================")
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
        graph.function_three(start_vertex, end_vertex)
    
    elif choice == 4:
        print("===========================================================")
        print("| Function 4:  Check the Minimum Spanning Tree (MST)      |")
        print("===========================================================")

        while True:
            print("Available Edges:", [i for i in graph.available_edges()], "\n")
            select_edge = str(input("\nSelect more available edge to generate MST? [y/n]")).lower()
            if select_edge == 'n':
                break
            elif select_edge == 'y':
                start_vertex = input("\nFrom: ")
                end_vertex = input("To: ")
                if graph.edge_input_validation(start_vertex, end_vertex) == True:
                    graph.function_four(start_vertex, end_vertex)
                    graph.print_graph()
            else:
                print("Invalid Input!")
        
    elif choice == 5:
        print("===========================================================")
        print("| Function 5:  Reset Graph                                 |")
        print("===========================================================")
        print_graph = str(input("Print graph after reset? [y/n]")).lower()
        if print_graph == 'y':
            graph.reset_graph(print_graph=True)
        else:
            graph.reset_graph()
    
    elif choice == 6:
        print("===========================================================")
        print("| Function 6:  Add New Edge                                |")
        print("===========================================================")
        while True:
            print("\nWhich edge would you like to add?")
            print("Available Edges:", [i for i in graph.available_edges()], "\n")
            start_vertex = input("From: ")
            end_vertex = input("To: ")
            if graph.edge_input_validation(start_vertex, end_vertex) == True:
                graph.add_new_edge(start_vertex, end_vertex)
                break
    
    elif choice == 7:
        print("===========================================================")
        print("| Function 7:  Remove Edge                                |")
        print("===========================================================")
        print("\nWhich edge would you like to remove?")
        print("Removable Edges:", [i for i in graph.removeable_edges()], "\n")
        start_vertex = input("From: ")
        end_vertex = input("To: ")
        graph.remove_edge(start_vertex, end_vertex)
    
    else:
        print("Something went wrong when taking user input, you have an input error. Try making an input again.")
        return
