"""
QUESTION:
Create a `sequential_graph_mapper` function in Python. Implement this function to take a list of graph mappers as input and return a function that takes a graph as input and executes each mapper sequentially on the input graph. If any mapper throws an error, the execution should stop, and the error should be propagated up.
"""

def sequential_graph_mapper(mappers):
    """
    Creates a function that takes a graph as input and executes each mapper sequentially on the input graph.
    
    Args:
        mappers (list): A list of graph mappers.
    
    Returns:
        function: A function that takes a graph as input and executes the graph mappers sequentially.
    """

    def mapper(graph):
        result = graph
        for func in mappers:
            try:
                result = func(result)
            except Exception as e:
                raise e
        return result
    
    return mapper