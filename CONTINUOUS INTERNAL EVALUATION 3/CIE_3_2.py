from collections import deque

class Graph:
    def __init__(self):
        
        self.adj_list = {}

    def add_vertex(self, vertex):
        
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
    
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        
        if start_vertex not in self.adj_list:
            print(f"Vertex {start_vertex} not in graph.")
            return
        
        visited = set()  
        queue = deque([start_vertex])  

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")  
                
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

print("Breadth-First Search starting from vertex 1:")
graph.bfs(1)

