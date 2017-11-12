class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def show(self):
        return self.id

    def add_neighbor(self, nbr, w):
        self.neighbors[nbr] = w

    def get_weight(self, nbr):
        if nbr in self.neighbors:
            return self.neighbors[nbr]

    def get_neighbors(self):
        return self.neighbors.keys()

class Graph:
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        if key not in self.graph:
            self.graph[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.graph:
            return self.graph[key]
        else:
            return None

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].add_neighbor(v, w)

    def show_vertices(self):
        return self.graph.keys()
