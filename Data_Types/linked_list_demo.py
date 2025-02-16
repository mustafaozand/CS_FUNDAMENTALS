class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

list_of_nodes = []

if __name__ == "__main__":
    node1 = Node("ozan", None)

    list_of_nodes.append(node1)    

    root = node1
    
    new_node = Node("ali", None)
    
    list_of_nodes.append(new_node)

    node_2_index = len(list_of_nodes) - 1

    tmp = root
    
    if new_node.data > tmp.data:
       tmp_next = tmp.next
       tmp.next = len(list_of_nodes) - 1
    else:
        new_node.next = tmp
        
