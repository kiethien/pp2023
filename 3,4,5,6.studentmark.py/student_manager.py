from student import*
from course import*

students = []
courses = []

def add_student():
    name = input('Enter student name: ')
    student_id = input('Enter student ID: ')
    student = Student(name, student_id)
    students.append(student)

    while True:
        choice = input('Do you want to add a course for this student? (Y/N): ')
        if choice.lower() == 'y':
            course_name = input('Enter course name: ')
            marks = input('Enter marks: ')
            student.add_course(course_name, int(marks))
        elif choice.lower() == 'n':
            break
        else:
            print('Invalid choice. Please try again.')

def add_course():
    course_name = input('Enter course name: ')
    course = Course(course_name)
    courses.append(course)

    while True:
        choice = input('Do you want to add a student to this course? (Y/N): ')
        if choice.lower() == 'y':
            student_id = input('Enter student ID: ')
            student = find_student_by_id(student_id)
            if student:
                course.add_student(student)
            else:
                print('Student not found. Please try again.')
        elif choice.lower() == 'n':
            break
        else:
            print('Invalid choice. Please try again.')

def display_students():
    for student in students:
        print(f'{student.name} ({student.student_id}):')
        for course_name, marks in student.courses.items():
            print(f' - {course_name}: {marks}')

def display_gpas():
    for student in students:
        gpa = student.calculate_gpa()
        print(f'{student.name} ({student.student_id}): {gpa}')

def find_student_by_id(student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None