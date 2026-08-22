import math

def calculate_grade(average):
    if average >= 90:
        return "A"
    if average >= 80 and average < 90:
        return "B"
    elif average >= 70 and average < 80:
        return "C"    
    else:
        return "F"

def analyze_student_data():
    
    #---------------------------
    school_name = "FAST NU AI"
    passing_threshold = 70.0
    is_active_session = True
    #---------------------------
    subjects = ["Programming", "Math", "Data Science"]
    student_record = {}       ## Important concept
    #-------------------------------------------------------
    print("===============================================")
    print("===============================================")
    print(f"--- Welcome to the {school_name} Analyzer ---")
    print("===============================================")
    print("===============================================\n")
    print("-------------------------------------")
    student_name = input("Enter Student Name: ")
    print("-------------------------------------")
    
    #--------------------------------------------------------
    
    total_score = 0
    
    for i in subjects:
        score = float(input(f"Enter score for {i}: "))
        student_record[i] = score      ## stores the data
        total_score = total_score + score
        
    average_score = total_score / len(subjects)
    round_average = math.ceil(average_score)
    final_grade = calculate_grade(round_average)
    
    print("----------------------------------------")
    print(f"Performance Summary of: {student_name}")
    print(f"Scores are: {student_record}")
    print(f"Average marks: {average_score:.2f} (Rounded number is {round_average})")
    print(f"Final Grade is: {final_grade}")
    print("----------------------------------------\n")
if __name__ == "__main__":
    analyze_student_data()