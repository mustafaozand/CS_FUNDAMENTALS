graph = [
    ["A", "B", 4],
    ["A", "C", 2],
    ["B", "C", 5],
    ["B", "D", 10],
    ["C", "D", 3],
    ["D", "E", 1]
]



def djikstra(graph, start, end):
    visited_nodes = []
    working_values = {
        start : 0
    }
    current_vertex = start

    while current_vertex != end: 

        for vertex in graph:
            if vertex[1] not in working_values:
                    working_values[vertex[1]] = 10000

        for neighbour in graph:
            if neighbour[0] == current_vertex and neighbour[1] not in visited_nodes:
                new_working_value = working_values[current_vertex] + neighbour[2]
                if new_working_value < working_values[neighbour[1]]:
                    working_values[neighbour[1]] = new_working_value

        next_vertex = None
        
        for possible_route in working_values:
            if possible_route not in visited_nodes:
                if next_vertex is None or working_values[possible_route] < working_values[next_vertex]:
                    next_vertex = possible_route

        if next_vertex is None:
            break

        visited_nodes.append(next_vertex)
        current_vertex = next_vertex
    
    return visited_nodes, working_values




       
            


visited_nodes, working_values = djikstra(graph, "A", "E")
                    
print(f"These are the nodes which have been visited: {visited_nodes} and the length of the route: {working_values["E"]}")

    

    

    
    

    


        


    
        
            

