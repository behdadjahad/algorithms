class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, source, destination):
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

        # For an undirected graph, you may want to add the reverse edge as well
        # If the graph is directed, you can omit the following lines
        if destination in self.graph:
            self.graph[destination].append(source)
        else:
            self.graph[destination] = [source]

    def print_graph(self):
        for vertex in self.graph:
            connections = " -> ".join(self.graph[vertex])
            print(f"{vertex} -> {connections}")

