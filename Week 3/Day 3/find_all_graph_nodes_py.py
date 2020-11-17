def csFindAllPathsFromAToB(graph):
    # since we need more information in order to recurse 
    # but we can't change this function signature 
    # we'll define a recursive helper function with the 
    # signature that we need 
    all_paths = []
    # we also need to keep track of the nodes we've already visited 
    visited = set() 
    
    recurse(graph, 0, [], all_paths, visited)
    
    return all_paths
    
def recurse(graph, current_node, path, all_paths, visited):
    # add the current_node to the path 
     
    # base case 1:
    # we've gone through every graph node 
    # if current_node > len(graph) - 1
    # add the current path we're building up to our list of `all_paths`
    # pop from our path 
    # return 
    
    # base case 2:
    # if the graph node has no neighbors
    # return 
    
    # add the current node to our visited set 
    
    # traverse through the node's neighbors 
	for neighbor in graph[current_node]:
        # for each neighbor, we need to recurse with that neighbor 
        
    # pop from our current path 