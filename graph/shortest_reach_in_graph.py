class Graph:
    def __init__(self, n):
        self.nodes = n
        self.graph = defaultdict(lambda: set())

    def connect(self, x, y):
        self.graph.setdefault(x, set()).add(y)
        self.graph.setdefault(y, set()).add(x)

    def find_all_distances(self, start, n):
        queue = [start]
        checked = []
        distances =[-1]*(self.nodes)
        distances[start] = 0
        while queue:
            val = queue[0]
            queue.remove(queue[0])
            if val in checked:
                continue
            checked.append(val)
            for x in self.graph[val]:
                if distances[x] == -1:
                    distances[x] = distances[val] + 6
                queue.append(x)
        distances.remove(distances[start])
        for value in distances:
            print(value, end=" ")
