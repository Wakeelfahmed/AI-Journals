def find_path(graph, str_Node, End_Node, path = []):
  path.append(str_Node)
  if str_Node == End_Node:
    return path

  if str_Node not in graph:
    return None

  for node in graph[str_Node]:
    if node not in path:
      newpath = find_path(graph, node, End_Node, path)
      if newpath:
        return newpath

  return None

#Main
graph = {'A': ['B', 'C'],
 'B': ['C', 'D'],
 'C': ['D','F'],
 'D': ['C','E'],
 'E': ['F'],
 'F': ['C','E']}

result_path = find_path(graph, 'A', 'E')
print(result_path)

