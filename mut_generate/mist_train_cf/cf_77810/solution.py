"""
QUESTION:
Create a program that uses two parallel arrays "students" and "grades" with the initial data: students = ["John", "Jane", "Emily", "Michael"] and grades = [85, 90, 92, 88]. Implement the following functions: add_student(name, grade), update_grade(name, grade), remove_student(name), display_students(), and calculate_average(). These functions should add a new student and grade, update a student's grade, remove a student, display all students and grades, and calculate the average grade respectively. If a student does not exist in the array, the program should handle this case and print a corresponding message.
"""

def entrance(students, grades):
    def add_student(name, grade):
        students.append(name)
        grades.append(grade)

    def update_grade(name, grade):
        if name in students:
            index = students.index(name)
            grades[index] = grade
        else:
            print("Student does not exist.")

    def remove_student(name):
        if name in students:
            index = students.index(name)
            students.remove(name)
            grades.pop(index)
        else:
            print("Student does not exist.")

    def display_students():
        for i in range(len(students)):
            print(f"Student: {students[i]}, Grade: {grades[i]}")

    def calculate_average():
        return sum(grades)/len(grades)

    return add_student, update_grade, remove_student, display_students, calculate_average

# Note: You would need to call the functions like this:
# add_student, update_grade, remove_student, display_students, calculate_average = entrance(["John", "Jane", "Emily", "Michael"], [85, 90, 92, 88])