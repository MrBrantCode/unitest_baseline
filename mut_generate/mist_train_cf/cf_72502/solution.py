"""
QUESTION:
Create a function `DemarcateBracketClusters` that takes an input string of nested brackets and returns a list of strings, where each string represents a cluster of balanced brackets. The input string may contain multiple levels of nesting and may include spaces, which should be ignored. The brackets are guaranteed to be balanced and do not nest within each other.
"""

def DemarcateBracketClusters(input_string):
    # Create an array to store bracket clusters
    bracket_clusters = []
    
    # Discriminate spaces in the string
    input_string = input_string.replace(" ", "")
    
    # Create a counter for tracking the depth of the clusters
    cluster_depth = 0
    
    # Create a temporary string to build bracket clusters
    cluster_string = ""
    
    # Scan the string and separate bracket clusters
    for character in input_string:
        if character == '(':
            cluster_depth += 1
        elif character == ')':
            cluster_depth -= 1
            
        # Append the current character to cluster string
        cluster_string += character
        
        # When the depth returns to 0, it indicates the end of a cluster
        if cluster_depth == 0:
            bracket_clusters.append(cluster_string)
            cluster_string = ""
            
    return bracket_clusters