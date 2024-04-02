class DWGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end, cost):
        if start in self.graph:
            self.graph[start].append((end, cost))
        else:
            print(f"Node {start} not found in the graph.")

    def find_path(self, start, end, path=[], total_cost=0):
        path = path + [start]

        if start == end:
            return path, total_cost

        if start not in self.graph:
            return None

        for neighbor, cost in self.graph[start]:
            if neighbor not in path:
                new_path, new_cost = self.find_path(neighbor, end, path, total_cost + cost)
                if new_path:
                    return new_path, new_cost

        return None

# Example usage:
if __name__ == "__main__":
    # Instantiate DWGraph object
    graph = DWGraph()

    # Add nodes
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        graph.add_node(node)

    # Add edges with costs
    edges = [('A', 'B', 2), ('A', 'C', 1), ('B', 'C', 2), ('B', 'D', 5),
             ('C', 'D', 1), ('C', 'F', 3), ('D', 'C', 1), ('D', 'E', 4),
             ('E', 'F', 3), ('F', 'C', 1), ('F', 'E', 2)]

    for edge in edges:
        graph.add_edge(*edge)

    # Find and print a path from 'A' to 'E'
    start_node = 'A'
    end_node = 'E'
    result_path, total_cost = graph.find_path(start_node, end_node)

    if result_path:
        print(f"Path from {start_node} to {end_node}: {result_path}")
        print(f"Total cost: {total_cost}")
    else:
        print(f"No path found from {start_node} to {end_node}.")
