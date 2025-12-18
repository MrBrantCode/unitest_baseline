"""
QUESTION:
Create a function called `organize_students` that takes a string of student information as input. The input string is a semicolon-separated list of students, where each student's information is comma-separated in the following order: name, age, grade, street, city, state, and zip. The function should return a dictionary with the keys "school" and "students". The "school" key should be set to the name of the school (which is assumed to be "ABC High School"), and the "students" key should be a list of dictionaries containing the information for each student. Each student dictionary should have the keys "name", "age", "grade", and "address", where "address" is another dictionary with the keys "street", "city", "state", and "zip".
"""

def organize_students(students):
    student_list = students.split(";")
    student_info = []
    for student in student_list:
        student_data = student.split(",")
        student_dict = {
            "name": student_data[0],
            "age": int(student_data[1]),
            "grade": int(student_data[2]),
            "address": {
                "street": student_data[3],
                "city": student_data[4],
                "state": student_data[5],
                "zip": student_data[6]
            }
        }
        student_info.append(student_dict)
    school_dict = {
        "school": "ABC High School",
        "students": student_info
    }
    return school_dict