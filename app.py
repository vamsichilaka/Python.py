students = []
student_names = set()


def calculate_average(marks):
    return sum(marks) / 3


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"


def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for i in range(1, 4):
            mark = float(input(f"Enter subject {i} mark: "))
            marks.append(mark)

        avg = calculate_average(marks)

        student = {
            "name": name,
            "marks": marks,
            "average": avg
        }

        students.append(student)
        student_names.add(name)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Marks must be numbers.")


def view_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        print("\n--- Student Report ---")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {grade(s['average'])}")


def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"] == name:
            print("\n--- Found Student ---")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Average: {s['average']:.2f}")
            return

    print("Student not found!")


def delete_student():
    name = input("Enter name to delete: ")

    global students

    for s in students:
        if s["name"] == name:
            students.remove(s)
            student_names.remove(name)
            print("Student deleted successfully!")
            return

    print("Student not found!")


while True:
    print("\n===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    except Exception as e:
        print(f"Unexpected error: {e}")
