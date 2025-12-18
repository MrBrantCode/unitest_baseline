"""
QUESTION:
Write a function `is_consistent(implications)` that takes a list of logical implications as input, where each implication is a string in the form "A(x) ⇒ B(x)" and A(x) and B(x) are predicates with alphanumeric characters and the variable x is the same in both A(x) and B(x). The function should return True if there exists an assignment of truth values to the predicates that satisfies all the implications, and False otherwise.
"""

def entance(implications):
    implications_dict = {}
    
    for imp in implications:
        A, B = imp.split(" ⇒ ")
        if A in implications_dict:
            implications_dict[A].append(B)
        else:
            implications_dict[A] = [B]
    
    def dfs(predicate, visited):
        if predicate not in implications_dict:
            return True
        if predicate in visited:
            return False
        visited.add(predicate)
        for imp in implications_dict[predicate]:
            if not dfs(imp, visited):
                return False
        visited.remove(predicate)
        return True
    
    for predicate in implications_dict:
        if not dfs(predicate, set()):
            return False
    return True