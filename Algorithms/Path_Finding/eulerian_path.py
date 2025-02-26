class EulerianPath:
    def __init__(self, edges):
        self.graph = {} # I will use a dictionary to store my adjacency list representing my graph
        self.edge_count = {} # Also a dectionary to store the valency of each vertex in my graph

        # Constructing the graph from an array of edges entered as a parameter to the object, and ensuring that the nodes are connected by non-directed edges.

        for u,v in edges:
            if u not in self.graph: 
                self.graph[u] = [] 

            if v not in self.graph:
                self.graph[v] = []

            self.graph[u].append(v) # e.g. 0:[1]
            self.graph[v].append(u) # 1:[0]

            self.edge_count[u] = self.edge_count.get(u, 0) +1 # since we have added the node into its adjacency list the edge_count must be incremented by 1, if it doesn't exist it will default to 0
            self.edge_count[v] = self.edge_count.get(v,0) +1


    def find_start_vertex(self):
        # We will find a valid starting vertex for the eulerian path
        start_vertex = None
        for vertex, degree in self.edge_count.items(): # .items() will convert the dictionary into a tuple, so that for one index vertex you can access the vertex and also access the degree.
            if degree % 2 == 1: 
                return vertex
            if start_vertex is None:
                start_vertex = vertex #any vertex in the graph

            return start_vertex #return once determined that no vertices with an odd valency exists
        

    def find_eulerian_path(self):
        # Performs the DFS traversal
        start = self.find_start_vertex()

        if start is None:
            return None
        
        stack = [start] # DFS uses a stack and BFS uses a dictionary

        path = [] # This will stor the Euclerian Path
        while stack:
            vertex = stack[len(stack)-1]

            if self.graph[vertex]:
                next_vertex = self.graph[vertex].pop()
                self.graph[next_vertex].remove(vertex) # Remove the vertex from the graph, to show tha it has been visited
                stack.append(next_vertex)

            else:
                path.append(stack.pop())

        return path[::-1] #reverse the path since the stack will have the first element removed very last.
            
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 1)]
eulerian_path_finder = EulerianPath(edges)
print(eulerian_path_finder.find_eulerian_path())