students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    students[student_id] = {
        "name": name,
        "subjects": {}
    }

    print("Student added successfully!")


def enter_grade():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    subject = input("Enter Subject: ")
    grade = float(input("Enter Grade: "))

    students[student_id]["subjects"][subject] = grade

    print("Grade added successfully!")


def calculate_average():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    subjects = students[student_id]["subjects"]

    if len(subjects) == 0:
        print("No grades entered.")
        return

    total = sum(subjects.values())
    average = total / len(subjects)

    print("Average Grade:", round(average, 2))


def view_grades():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\n--- STUDENT GRADES ---")
    print("Student ID:", student_id)
    print("Name:", student["name"])

    if len(student["subjects"]) == 0:
        print("No grades entered.")
        return

    for subject, grade in student["subjects"].items():
        print(subject, ":", grade)

    total = sum(student["subjects"].values())
    average = total / len(student["subjects"])

    print("Average:", round(average, 2))


def check_pass_fail():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    subjects = students[student_id]["subjects"]

    if len(subjects) == 0:
        print("No grades entered.")
        return

    total = sum(subjects.values())
    average = total / len(subjects)

    print("Average Grade:", round(average, 2))

    if average >= 75:
        print("Status: PASSED")
    else:
        print("Status: FAILED")


while True:
    print("\n==============================")
    print("     GRADE MONITORING SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. Enter Subject and Grade")
    print("3. Calculate Average")
    print("4. View Student Grades")
    print("5. Check Pass/Fail")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        enter_grade()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        view_grades()

    elif choice == "5":
        check_pass_fail()

    elif choice == "6":
        print("Thank you for using the Grade Monitoring System!")
        break

    else:
        print("Invalid choice!")
        