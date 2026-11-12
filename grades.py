def add_grade(students, name, grade):
    for s in students:
        if s['name'].lower() == name.lower():
            if 'grades' not in s:
                s['grades'] = []
            s['grades'].append(grade)
            print(f"{s['name']} ga {grade} baho qo'shildi.")
            return
    print(f"'{name}' topilmadi.")

def calculate_average_grade(students, name):
    for s in students:
        if s['name'].lower() == name.lower():
            grades = s.get('grades', [])
            if not grades:
                return f"{s['name']} da baholar mavjud emas."
            return sum(grades) / len(grades)
    return f"'{name}' topilmadi."

def get_top_student(students):
    if not students:
        return "Talabalar mavjud emas."
    
    top_student = None
    highest_avg = -1
    
    for s in students:
        grades = s.get('grades', [])
        if not grades:
            continue
        avg = sum(grades) / len(grades)
        if avg > highest_avg:
            highest_avg = avg
            top_student = s
            
    if not top_student:
        return "Baholangan talabalar yo'q."
    return f"Eng yuqori o'rtacha baho: {top_student['name']} ({highest_avg})"