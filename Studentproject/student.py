import json

students = []


def add_student():

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student Added Successfully")


def view_students():

    if len(students) == 0:
        print("No Students Found")

    else:

        for student in students:

            print("----------------")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])


def search_student():

    search_name = input("Enter Student Name: ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("Student Found")
            print(student)

            found = True

    if not found:
        print("Student Not Found")


def delete_student():

    name = input("Enter Student Name to Delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student Deleted")
            return

    print("Student Not Found")


def save_data():

    with open("students.json", "w") as file:

        json.dump(students, file)

    print("Data Saved")


def load_data():

    global students

    try:

        with open("students.json", "r") as file:

            students = json.load(file)

    except FileNotFoundError:

        students = []


load_data()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        save_data()

    elif choice == "6":

        save_data()

        print("Exiting Program")
        break

    else:
        print("Invalid Choice")