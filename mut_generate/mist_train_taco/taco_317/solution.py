"""
QUESTION:
Given two force vectors, find out whether they are parallel, perpendicular or neither. Let the first vector be A = a_{1} i +a_{2} j + a_{3} k and the second vector be B = b_{1} i + b_{2} j + b_{3} k.
A.B = a_{1 }* b_{1} + a_{2 }* b_{2} + a_{3 }* b_{3}
A x B = (a2 * b3 - a_{3 }* b_{2}) i - (a_{1} * b_{3} - b_{1}* a_{3}) j + (a_{1 }* b_{2} - a_{2 }* b_{1}) k
|A|^{2} = a12 + a22 + a32
If A.B = 0, then A and B are perpendicular.
If |A X B|^{2} = 0, then A and B are parallel.
Example 1:
Input: A = 3i + 2j + k, B = 6i + 4j + 2k
Output: 1
Explanation: |A X B|^{2 }= 0
Example 2:
Input: A = 4i + 6j + k, B = i - 1j + 2k
Output: 2
Explanation: A.B = 0
 
Your Task:
You don't need to read or print anything. Your task is to complete the function find() which takes A and B vector as parameter and returns 1 if they are parallel to each other, 2 if they are perpendicular to each other or 0 otherwise. A and B vectors will contain (a1,a2,a3) and (b1,b2,b3) respectively.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
-100 <= Component <= 100
"""

def determine_vector_relationship(A, B):
    # Calculate the dot product (parallel check)
    dot_product = A[0] * B[0] + A[1] * B[1] + A[2] * B[2]
    
    # Calculate the cross product (perpendicular check)
    cross_product = [
        A[1] * B[2] - A[2] * B[1],
        A[0] * B[2] - A[2] * B[0],
        A[0] * B[1] - A[1] * B[0]
    ]
    
    # Calculate the magnitude squared of the cross product
    cross_product_magnitude_squared = sum(i ** 2 for i in cross_product)
    
    # Determine the relationship
    if cross_product_magnitude_squared == 0:
        return 1  # Vectors are parallel
    elif dot_product == 0:
        return 2  # Vectors are perpendicular
    else:
        return 0  # Vectors are neither parallel nor perpendicular