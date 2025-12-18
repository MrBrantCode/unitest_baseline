"""
QUESTION:
Implement a function `compare_versions(version1: str, version2: str) -> str` that compares two version strings following semantic versioning rules. The function should return "1" if version1 is greater than version2, "-1" if version1 is less than version2, or "0" if they are equal. Each version string is a series of numbers separated by periods.
"""

def entance(version1: str, version2: str) -> str:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    
    for i in range(max(len(v1), len(v2))):
        num1 = v1[i] if i < len(v1) else 0
        num2 = v2[i] if i < len(v2) else 0
        
        if num1 > num2:
            return '1'
        elif num1 < num2:
            return '-1'
    
    return '0'