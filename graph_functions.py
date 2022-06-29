class Graph:
    # Constructor to initialize the matrix
    def __init__(self, size):
        self.adjacency_mat = []
        for i in range(size):
            self.adjacency_mat.append([0 for i in range(size)])
        self.size = size

    # Add edges from vertex 1 to vertex 2, with a default weight of 1
    def add_edges(self, v1, v2, weight=1):
        if v1 == v2:
            print(f"{v1} and {v2} are the vertices!")
        self.adjacency_mat[v1][v2] = weight

    # Remove edges
    def remove_edges(self, v1, v2):
        if self.adjacency_mat[v1][v2] == 0:
            print(f"No edge between vertex {v1} and {v2}")
        self.adjacency_mat[v1][v2] = 0

    # Print the matrix
    def print_matrix(self):
        vertex_list = [" ", "LA", "BL", "SB", "RM", "MV"]
        for vertex in vertex_list:
            print("{:4}".format(vertex), end=' ')
        print()

        for i, row in enumerate(self.adjacency_mat):
            print(vertex_list[i+1], end=' ')
            for val in row:
                print("{:4}".format(val), end=' ')
            print()