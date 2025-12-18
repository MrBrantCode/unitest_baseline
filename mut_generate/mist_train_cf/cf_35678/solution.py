"""
QUESTION:
Implement a function `grayCodeGenerator(method, n)` that generates a sequence of Gray codes of length `2^n` using the specified `method`. The function should support two methods: "symmetrical" and "xor". The "symmetrical" method should use a symmetrical generation approach, while the "xor" method should use the XOR operation. The function should return a list of integers representing the Gray code sequence.
"""

def grayCodeGenerator(method, n):
    if method == "symmetrical":
        def grayCodeSymmetricalGeneration(n):
            if n <= 0:
                return [0]
            else:
                result = grayCodeSymmetricalGeneration(n - 1)
                mask = 1 << (n - 1)
                for i in range(len(result) - 1, -1, -1):
                    result.append(result[i] | mask)
                return result
        return grayCodeSymmetricalGeneration(n)
    elif method == "xor":
        result = []
        for i in range(2**n):
            result.append(i ^ (i >> 1))
        return result