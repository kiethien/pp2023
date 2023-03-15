class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.enrollments = {}
        
    def enroll_in_course(self, course):
        enrollment = Enrollment(self, course)
        self.enrollments[course.id] = enrollment
        course.add_enrollment(enrollment)
        
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.enrollments = []
        
    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)
        
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.marks = {}
        
    def add_mark(self, mark):
        self.marks[mark.course.id] = mark
        
class Mark:
    def __init__(self, course, mark):
        self.course = course
        self.mark = mark
        
class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_course(self, course):
        self.courses.append(course)
        
    def add_mark(self, student_id, course_id, mark):
        for enrollment in self.get_enrollments(student_id, course_id):
            mark_obj = Mark(enrollment.course, mark)
            enrollment.add_mark(mark_obj)
                
    def list_students(self):
        for student in self.students:
            print(f"{student.id}: {student.name} ({student.dob})")
            
    def list_courses(self):
        for course in self.courses:
            print(f"{course.id}: {course.name}")
            
    def show_marks(self, student_id):
        for course in self.get_courses_for_student(student_id):
            for enrollment in self.get_enrollments(student_id, course.id):
                mark = enrollment.marks.get(course.id)
                if mark is not None:
                    print(f"{enrollment.student.name} ({enrollment.student.id}) - {course.name}: {mark.mark}")
                else:
                    print(f"{enrollment.student.name} ({enrollment.student.id}) - {course.name}: no mark")
                
    def get_enrollments(self, student_id, course_id):
        enrollments = []
        for student in self.students:
            if student.id == student_id:
                enrollment = student.enrollments.get(course_id)
                if enrollment is not None:
                    enrollments.append(enrollment)
        return enrollments
    
    def get_courses_for_student(self, student_id):
        courses = set()
        for student in self.students:
            if student.id == student_id:
                for enrollment in student.enrollments.values():
                    courses.add(enrollment.course)
        return courses

def case_switch(x):
    def switch(self, choice):
        default = 'Pls choose again'
        return getattr(self, 'case_' +str(choice) , lambda: default)()
    
    def case_1(self):
        MarkManager.add_course(input("Enter a new course: "))

    def case_2(self):
        MarkManager.add_student(input("Enter student info"))

student_temp = None
student_temp2 = None
student_temp3 = None
student_temp = input("Enter id: ")
student_temp2 = input("Enter name: ")
student_temp3 = input("Enter dob: ")
Student(student_temp,student_temp2,student_temp3)
MarkManager.add_student(Student())
MarkManager.list_students