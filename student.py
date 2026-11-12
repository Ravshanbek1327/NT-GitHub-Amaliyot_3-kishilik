students = []



def add_student(name, age, grade):

    students.append({"name": name, "age": age, "grade": grade})

    print(f"{name} qo'shildi.")



def show_all_students():

    if not students:

        print("Talabalar yo'q.")

        return

    for i, s in enumerate(students, 1):

        print(f"{i}. {s['name']} - {s['age']} yosh, Bahosi/Guruh: {s['grade']}")



def search_student_by_name(name):

    izlash = [s for s in students if name.lower() in s['name'].lower()]

    if not izlash:

        print(f" '{name}' topilmadi.")

        return

    for s in izlash:

        print(f"{s['name']} - {s['age']} yosh, Bahosi/Guruh: {s['grade']}")