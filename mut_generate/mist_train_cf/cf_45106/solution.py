"""
QUESTION:
Find a specific group of hexadecimal numbers within a larger sequence that, when multiplied together, give a predetermined result. The function to complete this task should be named `find_hex_cluster`. The function will take a string of hexadecimal digits and a target product as inputs and return the specific group of hexadecimal numbers as a string.
"""

def find_hex_cluster(hex_string, target):
    def product(cluster):
        result = 1
        for num in cluster:
            result *= int(num, 16)
        return result

    for length in range(1, len(hex_string)):
        for i in range(len(hex_string) - length + 1):
            cluster = [hex_string[i:i+length]]
            current_product = product(cluster)
            if current_product > target:
                break
            j = i + length
            while current_product < target and j < len(hex_string):
                cluster.append(hex_string[j:j+1])
                current_product = product(cluster)
                if current_product == target:
                    return ''.join(cluster)
                j += 1
    return None