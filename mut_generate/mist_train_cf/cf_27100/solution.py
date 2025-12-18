"""
QUESTION:
Write a function `CountDeepestNamespaces` that takes a string representing C# code and returns a dictionary where the keys are the deepest level namespaces and the values are the counts of occurrences of each namespace at that level. The input C# code is assumed to be well-formed and syntactically correct.
"""

import re

def CountDeepestNamespaces(code):
    namespace_pattern = r'namespace\s+([\w.]+)\s*{'
    matches = re.findall(namespace_pattern, code)
    namespace_counts = {}
    
    deepest_level = 0
    for namespace in matches:
        levels = namespace.count('.')
        if levels > deepest_level:
            deepest_level = levels
    
    deepest_namespaces = [namespace for namespace in matches if namespace.count('.') == deepest_level]
    
    for namespace in deepest_namespaces:
        if namespace in namespace_counts:
            namespace_counts[namespace] += 1
        else:
            namespace_counts[namespace] = 1
    
    return namespace_counts