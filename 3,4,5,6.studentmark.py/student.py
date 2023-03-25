class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def add_course(self, course_name, marks):
        self.courses[course_name] = marks

    def calculate_gpa(self):
        total_gpa = 0
        num_courses = len(self.courses)

        for course_name in self.courses:
            total_gpa += self.courses[course_name]

        gpa = total_gpa / num_courses
        return round(gpa, 2)