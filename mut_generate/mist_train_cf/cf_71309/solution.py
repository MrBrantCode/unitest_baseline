"""
QUESTION:
Given an array of students where each `students[i] = [wi, ki]` represents the `ith` student of weight `wi` with exactly `ki` other students in front who have a weight greater than or equal to `wi`, reconstruct and return the line that is represented by the input array `students`. The returned line should be formatted as an array `line`, where `line[j] = [wj, kj]` is the attributes of the `jth` student in the line (`line[0]` is the student at the front of the line). The length of `students` is between 1 and 2000 (inclusive) and `0 <= wi <= 106` and `0 <= ki < students.length`.
"""

def reconstructQueue(students):
    students.sort(key=lambda x: (-x[0], x[1]))
    output = []

    for student in students:
        output.insert(student[1], student)
    
    return output