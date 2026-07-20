students = []
next_id = 1

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['id']},{student['name']},{student['age']},{student['language']}\n")

def load_students():
    global students, next_id
    students = []
    next_id = 1
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 4:
                    sid, name, age, language = parts
                    student = {
                        "id": int(sid),
                        "name": name,
                        "age": age,
                        "language": language
                    }
                    students.append(student)
                    if int(sid) >= next_id:
                        next_id = int(sid) + 1
    except FileNotFoundError:
        pass

def is_valid_language(lang):
    return bool(lang) and all(c.isalpha() or c.isspace() for c in lang)

def add_student():
    global next_id
    
    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Name cannot be empty.")
    
    while True:
        age = input("Age: ").strip()
        if age.isdigit():
            break
        print("Age must be a number.")
    
    while True:
        language = input("Language: ").strip()
        if is_valid_language(language):
            break
        print("Language must contain only letters and spaces (e.g., 'Python', 'Java Script').")
    
    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "language": language
    }
    students.append(student)
    next_id += 1
    save_students()
    print(f"Student added successfully! ID: {student['id']}")

def show_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("-------------------")
            print("ID:", student.get("id"))
            print("Name:", student.get("name"))
            print("Age:", student.get("age"))
            print("Language:", student.get("language"))

def search_student():
    if len(students) == 0:
        print("No students found.")
        return
    search_name = input("Enter name: ").strip().lower()
    found = False
    for student in students:
        if student.get("name", "").lower() == search_name:
            print("-------------------")
            print("ID:", student.get("id"))
            print("Name:", student.get("name"))
            print("Age:", student.get("age"))
            print("Language:", student.get("language"))
            found = True
    if not found:
        print("Student not found.")

def delete_student():
    if len(students) == 0:
        print("No students found.")
        return
    try:
        sid = int(input("Enter student ID to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    for i, student in enumerate(students):
        if student.get("id") == sid:
            students.pop(i)
            save_students()
            print("Student deleted successfully.")
            return
    print("Student not found.")

def edit_student():
    if len(students) == 0:
        print("No students found.")
        return
    try:
        sid = int(input("Enter student ID to edit: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    for student in students:
        if student.get("id") == sid:
            print("Leave blank to keep current value.")
            new_name = input(f"New Name (current: {student.get('name')}): ").strip()
            new_age = input(f"New Age (current: {student.get('age')}): ").strip()
            new_language = input(f"New Language (current: {student.get('language')}): ").strip()
            
            if new_name:
                student["name"] = new_name
            if new_age:
                if new_age.isdigit():
                    student["age"] = new_age
                else:
                    print("Age must be a number. Keeping old age.")
            if new_language:
                if is_valid_language(new_language):
                    student["language"] = new_language
                else:
                    print("Language must contain only letters and spaces. Keeping old language.")
            
            save_students()
            print("Student updated successfully.")
            return
    print("Student not found.")

def count_students():
    print("Total Students:", len(students))

def main():
    load_students()
    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Edit Student")
        print("6. Count Students")
        print("7. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            edit_student()
        elif choice == "6":
            count_students()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()