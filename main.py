import json
from student import students, add_student, show_all_students, search_student_by_name
from grades import add_grade, calculate_average_grade, get_top_student

def load_from_json(filename="students.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_to_json(students_list, filename="students.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students_list, f, ensure_ascii=False, indent=4)

def main():
    global students
    students = load_from_json()
    
    while True:
        print("\n1. Talaba qo'shish")
        print("2. Talabalarni ko'rsatish")
        print("3. Talaba qidirish")
        print("4. Baho qo'shish")
        print("5. O'rtacha bahoni hisoblash")
        print("6. Eng yuqori baho olgan talaba")
        print("0. Chiqish")
        
        choice = input("Tanlovni kiriting: ")
        
        if choice == "1":
            name = input("Ism: ")
            age = input("Yosh: ")
            grade = input("Bahosi/Guruh: ")
            add_student(name, age, grade)
            save_to_json(students)
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            search_student_by_name(name)
        elif choice == "4":
            name = input("Talaba ismi: ")
            g = float(input("Baho: "))
            add_grade(students, name, g)
            save_to_json(students)
        elif choice == "5":
            name = input("Talaba ismi: ")
            res = calculate_average_grade(students, name)
            print(res)
        elif choice == "6":
            res = get_top_student(students)
            print(res)
        elif choice == "0":
            save_to_json(students)
            break
        else:
            print("Noto'g'ri tanlov.")

if __name__ == "__main__":
    main()