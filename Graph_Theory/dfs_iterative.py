from Stack import Stack 


graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "E", "F"],
    "E": ["B", "D"],
    "F": ["C", "D"]
}

def dfs_iter(graph, start_node):
    stack = Stack(size=20)
    stack.push(start_node)

    visited = {}
    visited_list = []

    for node in graph:
        visited[node] = False

    while not stack.is_Empty():
        current_node = stack.pop()

        if not visited[current_node]:
            print(f"Visited: {current_node}")
            visited[current_node] = True
            visited_list.append(current_node)

            for neighbour in graph[current_node]:
                if not visited[neighbour]:
                    stack.push(neighbour)
    return visited_list



print(dfs_iter(graph, "A"))


        


    
        








    

