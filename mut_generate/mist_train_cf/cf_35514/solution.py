"""
QUESTION:
Implement the `depth_limited_search` function to perform a depth-limited search on a game tree. The function should take in three parameters: a `game` object with a `call_counter` attribute and a `root` node, a `depth_limit` to control the search depth, and an `expected_node_count` for verification. The function should recursively explore the game tree up to the specified depth limit, update the `game.call_counter` attribute with the number of nodes visited, and print a message indicating whether the visited nodes match the expected node count.
"""

def depth_limited_search(game, depth_limit, expected_node_count):
    def explore(node, depth):
        if depth == depth_limit:
            return 1  
        total_nodes = 1  
        for child in node.children:
            total_nodes += explore(child, depth + 1)
        return total_nodes

    visited_nodes = explore(game.root, 0)
    game.call_counter = visited_nodes
    if visited_nodes == expected_node_count:
        print("That's right! Looks like your depth limit is working!")
    else:
        print("Uh oh...looks like there may be a problem.")