"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).

You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.
"""

colors = ['Yellow', 'Blue', 'Red', 'Green', 'Purple']

# Definition for a graph node.
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.color = None


# O(V * E)
def color_graph(graph, colors):
    # Your code here
    # 1. color every graph node a different color 
    
    # how do we minimize the number of colors used? 
    # for the first node, any color is fine, since none of the neighbors 
    # have been colored yet 
    # as we continue iterating through our graph, we need to figure out
    # what colors are illegal for the given node 
    # we can iterate through the node's neighbors to see which ones are colored 
    # build up a set of illegal colors for every node 

    # two independant variables:
    # the number of nodes 
    # the number of connections 

    # O(V) where V is the number of vertices/nodes 
    for node in graph:
        illegal_colors = set()

        # O(E) where E is the number of connections/edges 
        for neighbor in node.neighbors:
            if neighbor.color is not None:
                illegal_colors.add(neighbor.color)

        # figure out which color(s) from the colors list is not in this illegal set
        # of colors for the given node 
        # assign its color to that color
        # O(E) since in the worst case we could color every node a different color 
        for color in colors:
            if color not in illegal_colors: # O(1)
                node.color = color
                break


g1 = GraphNode('G1')
g2 = GraphNode('G2')
g3 = GraphNode('G3')
g4 = GraphNode('G4')
g5 = GraphNode('G5')

g1.neighbors.add(g2)
g1.neighbors.add(g4)
g1.neighbors.add(g3)

g2.neighbors.add(g1)
g2.neighbors.add(g4)
g2.neighbors.add(g5)

g3.neighbors.add(g1)
g3.neighbors.add(g5)
g3.neighbors.add(g4)

g4.neighbors.add(g1)
g4.neighbors.add(g2)
g4.neighbors.add(g3)
g4.neighbors.add(g5)

g5.neighbors.add(g2)
g5.neighbors.add(g3)
g5.neighbors.add(g4)

graph = [g1, g2, g3, g4, g5]

color_graph(graph, colors)

for node in graph:
    print(node.color)
