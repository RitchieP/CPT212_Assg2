def homepage():
    # Welcome Message
    print("\t*********************************************************")
    print("\t*\tWELCOME TO CPT212 GROUP XX's ASSIGNMENT 2\t*")
    print("\t*********************************************************")
    print("\nTHIS PROGRAMME DEMONSTRATES SEVERAL GRAPH FUNCTIONS \n")
    
  
# Prompt user to choose a function to perform   
def user_input():
    # Menu of selection
    print("\n1 - Determine Strong Connectivity" +
          "\n2 - Cycle Detection" +
          "\n3 - Determine Shortest Path" +
          "\n4 - Compute Minimum Spanning Tree" +
          "\n5 - Add New Edge" +
          "\n6 - Remove Edge" +
          "\n7 - Reset Graph" +
          "\n8 - Exit")
    print("\nWhich function would you like to apply on the graph?\n")    
    
    # Input Validation
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice < 1 or choice > 8:
                raise ValueError 
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 - 8.")
        
    return choice