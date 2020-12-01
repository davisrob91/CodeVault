#!/usr/bin/python3

# Finding and Creating Adjacent Nodes
#
# A node is represented by a list where the positions in the list
# indicate which other nodes a particular node is connected to.
# A node cannot be connected to itself and will therefore have a 
# 0 in the position that corresponds to the 2D list. 
# 
# Each node must contain a list of all nodes.
# 
# 1-way association
# [[0, 1, 1, 0],
# [0, 0, 1, 1],
# [0, 0, 0, 1],
# [1, 0, 0, 0]]
# 
# 2-way association
# [[0, 1, 0, 0],
# [1, 0, 1, 1],
# [0, 1, 1, 0],
# [0, 1, 0, 0]]
#

import random
import time

def _print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def create_adjacent_nodes(nodes, directed=False):
    """
    Generate a 2D list representation of connected nodes.
    """

    matrix = []

    # Iterate of nodes by nodes to generate a correct undirected matrix.
    for y in range(nodes):
        node = []
        for x in range(nodes):
            if x == y:
                node.append(0)
            else:
                node.append(random.randrange(2))
        if directed:
            for d in range(y):
                node[d] = matrix[d][y]

        matrix.append(node)

    return matrix


def create_adjacent_directed_nodes_fast(nodes):
    """
    Same as create_adjacent_nodes(directed=True) but with a time
    complexity of (n(n-1))/2
    """

    matrix = [[0]*nodes]*nodes

    for y in range(nodes):
        matrix[y][y] = 0
        matrix[y][nodes-1-y] = matrix[nodes-1-y][y] = random.randrange(2)

    return matrix
        

def are_connected(matrix, node1, node2):
    """
    Determines the relationship of two nodes in a matrix.

        True:
            node1 <-> node2
            node1 -> node2
            node1 <- node2
        False
    """

    max_len = len(matrix)
    if node1 >= max_len or node2 >= max_len:
        return False
    if matrix[node1][node2] and matrix[node2][node1]:
        return 'node 1 <-> node 2'
    elif matrix[node1][node2]:
        return 'node 1 -> node 2'
    elif matrix[node2][node1]:
        return 'node 1 <- node 2'
    return False

    
def print_help():
    s = """
        AdjacentNodes.py -p|-h numNodes

        p - Print pretty, show all matrices created
        h - show this message

        numNodes - Number of nodes in all matrices.
        """

    print(s)
    exit(0)

if __name__ == '__main__':

    import sys

    pretty = False
    nodes = 1
    for arg in sys.argv[1:]:
        if arg == '-p':
            pretty = True
        elif arg == '-h':
            print_help()
        elif arg.isnumeric():
            nodes = int(arg)
        else:
            print_help()

    undirected = create_adjacent_nodes(nodes)

    before = time.time() 
    directed = create_adjacent_nodes(nodes, directed=True)
    after = time.time()
    print('time to create matrix %s us.' %
         str((after - before)*1E6))

    print('Creating fast directed %dx%d matrix.' % (nodes, nodes))
    before = time.time()
    fast = create_adjacent_directed_nodes_fast(nodes)
    after = time.time()
    print('time to create matrix %s us.' %
         str((after - before)*1E6))
   
    if pretty:
        _print_matrix(undirected)
        _print_matrix(directed)
        _print_matrix(fast)
    
    node_x = random.randrange(nodes)
    node_y = random.randrange(nodes)

    _print_matrix(undirected)
    print('Are %d and %d connected?' % (node_x, node_y))
    print(are_connected(undirected, node_x, node_y))






