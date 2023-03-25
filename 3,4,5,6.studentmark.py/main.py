from student_manager import *

def get_choice():
    print('What would you like to do?')
    print('1. Add a student')
    print('2. Add a course')
    print('3. Display list of students and their marks')
    print('4. Display list of students and their GPAs')
    print('5. Find student by id: ')
    print('6. Quit')
    choice = input('Enter your choice: ')
    return choice

def main():
    print('Welcome to the Student Management System!')
    while True:
        choice = get_choice()
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            display_students()
        elif choice == '4':
            display_gpas()
        elif choice == '5':
            find_student_by_id()
        elif choice == '6':
            print('Data saved successfully.')
            print('Thank you for using the Student Management System!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()