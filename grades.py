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
                return student
                
        else:    
            print("Student not found, try again")
            
def get_letter_grade(score):
    
    if 90 <= score < 100 : return "A"
    elif 80 <= score :return  "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    elif score < 60: return "F"
    else : return "Invalid"

student = student_search()
name = student["name"]
score = student["score"]
grade = get_letter_grade(score)



print(f" {name}'s score is {score}, and their grade is {grade}")


        


 







