student_info = {
    "name": "Akshay Kumar",  # string 
    "current_semester": 5,  # integer 
    "batch_year": 2025,  # integer 
    "current_year": 2023,  # integer 
    "hobbies": ["sports", "travelling"],  # list 
    "grade_12th": 94.0,  # float 
    "pursuing_btech": True  # boolean 
}

print("Name:", student_info["name"])  # Accessing string 
print("Current Semester:", student_info["current_semester"])  # Accessing integer 
print("Batch Year:", student_info["batch_year"])  # Accessing integer 
print("Current Year:", student_info["current_year"])  # Accessing integer 
print("Hobbies:", ", ".join(student_info["hobbies"]))  # Accessing list 
print("Grade in 12th:", student_info["grade_12th"])  # Accessing float 
print("Pursuing BTech:", student_info["pursuing_btech"])  # Accessing boolean 