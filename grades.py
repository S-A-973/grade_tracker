
# A list of dictionaries to store all the students data. ie names and scores.
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

def ask_for_name():
# Gets an input from the user: basically asks for students name
    while True:
        name = input("Please enter the students name: ").strip().capitalize()
        if name.isalpha():
            return name
        else:
            print("Invalid please use words to enter students name")


def student_search():
# Using the provided name to search the dictionaries
    while True:
        name = ask_for_name()

        for student in student_score:
            if student.get("name") == name:
                return student    
        else:    
            print("Student not found, try again")

       
def get_letter_grade(score):
# Converts a students score into a grade 
    if not 0 <= score <= 100: return "Invalid"
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"
    
def main():
    student = student_search()
    name = student["name"]
    score = student["score"]
    grade = get_letter_grade(score)
    print(f"{name}'s score is {score}, and their grade is {grade}")

if __name__ == "__main__":
    main()



    










