##This a grade tracker system to challange my knowledge on loops, lists, functions, variables.
student_score = [
    {"name":"Amina", "score": 88},
    {"name":"Brian", "score": 72},
    {"name":"Chloe", "score": 95},
    {"name":"David", "score": 64},
    {"name":"Esther", "score": 81},
    {"name":"Farid", "score": 58},
    {"name":"Grace", "score": 90},
    {"name":"Hassan", "score": 77},
    {"name":"Imani", "score": 69},
    {"name":"James", "score": 84}

]
def user_search_db():
    while True:
        name = input("Please enter the students name: ").strip().title()
        if name.isalpha():
            return name
            break
        else:
            print("Invalid please enter actual students name")

def student_search():
    while True:
        name = user_search_db()

        for student in student_score:
            if student.get("name") == name:
                print (f"{name} found ")
                return name
        else:    
            print("Student not found, try again")



        

student_search()
 





"""def get_letter_grade (): 
    for student, score in student_grades.items():
        if 90 >= score < 100 : return "A"
        elif 80 >= score :return  "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        elif score < 60: return "F"
        else : return "Invalid"

letter_grade = get_letter_grade()
for student, score in student_grades.items():
    print (student, score, letter_grade)
        
"""
