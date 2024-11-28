from Stack import Stack

visited_list = []
stack = Stack()

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "E", "F"],
    "E": ["B", "D"],
    "F": ["C", "D"]
}

def find_unvisited_node(graph, node):
    print(node)
    list_of_adjacent_nodes = graph[node]
    index = 0
    while index < len(list_of_adjacent_nodes):
        if not (list_of_adjacent_nodes[index] in visited_list):
            return list_of_adjacent_nodes[index]

        index += 1

    return None           

 

def dfs_iter(graph, start_node):
    current_node = start_node

    while current_node is not None:
        unvisited_node = find_unvisited_node(graph=graph, node=current_node)
        if unvisited_node is not None:
            stack.push(current_node)
            visited_list.append(current_node)
            current_node = unvisited_node

        else:
            if current_node not in visited_list:
                visited_list.append(current_node)
            current_node = stack.pop()
        

if __name__ == "__main__":
    dfs_iter(graph, "A")
    print(visited_list)



