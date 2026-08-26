import random
import json

print("=====================")
print("Student Grade Manager")
print("=====================")

teacher_name = input("What is your name: ").title()
running = True


print()
print(f"Hello {teacher_name}! Welcome to your very own Student Grade Manager!")
print()

with open("students.json", "r") as var_file:
    students = json.load(var_file)
    
        
while running:
    print("1. Add student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Search for student")
    print("5. Add Grade")
    print("6. Exit")
    print()

    option_num = int(input("What would you like to do? "))

    if option_num == 1:
        added_student = input("Student first and last name: ").title()
        student_age = int(input("Enter student age: "))
        student_id = random.randint(10000, 99999)
            
        duplicate_ID = True
        while duplicate_ID:
            duplicate_ID = False
            
            for student in students:
                if student_id == student["Student ID"]:
                    duplicate_ID = True
                    student_id = random.randint(10000, 99999)
                    break
               
                
        
        new_student = {
            "name": added_student,
            "age": student_age,
            "Student ID": student_id,
            "Grades": {
                "Homework": [],
                "Quizzes": [],
                "Participation": [],
                "Projects": [],
                "Tests": []
            }
        }
        students.append(new_student)
        students.sort(key=lambda student: student["name"])
    
        
        with open("students.json", "w") as var_file:
            json.dump(students, var_file, indent = 4)

        print(f"{added_student} has been added to your class!")
        


    elif option_num == 2:
        students.sort(key=lambda student: student["name"])
        print("----------------")
        print(f"{teacher_name}'s Class List!")
        print("----------------")
        
        
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Student ID: {student['Student ID']}")
            print(f"Grades: {student['Grades']}")
            print()
    
        

    elif option_num == 3:
        var_remove = int(input("Enter student ID: "))
        
        student_found = False
        
        for student in students:
            if var_remove == student["Student ID"]:
                student_found = True
                var_confirmation = input(f"Are you sure you'd like to remove {student['name']} and all their data from your class? ").title()
                if var_confirmation == "Yes":
                    students.remove(student)
                    print(f"{student['name']} ({student['Student ID']}) from your has been removed from your class.")

                    with open("students.json", "w") as var_file:
                        json.dump(students, var_file, indent = 4)

                break

        if student_found == False:
            print("Student does not exist.")
            


    elif option_num == 4:
        var_search = input("Search student name: ").title()
        student_found = False
        matching_students = []

        for student in students:
            if var_search == student["name"]:
                matching_students.append(student)
     
        edit_confirm = "No"
        if len(matching_students) == 0:
            print("Student not found.")

        elif len(matching_students) == 1:
            student = matching_students[0]
            print(f"{student['name']} ({student['Student ID']}) is enrolled in this class.")
            edit_confirm = input("Would you like to edit this student? ").title()

        elif len(matching_students) >= 2:
                print("There are multiple students found:")
                for student in matching_students: 
                    print(f"{student['name']} ({student['Student ID']})")
                ID_specification = int(input("Enter ID of student you are looking for: ")) 
                

                for student in matching_students:
                    if ID_specification == student["Student ID"]:
                        edit_confirm = input("Would you like to edit this student? ").title()   
                        break
                else:
                    print("Student not found.")    
                
        
        if edit_confirm == "Yes":
            edit_option = input("What would you like to edit (name or age)? ").title()

            if edit_option == "Name":
                        edit_name = input("Enter students new name: ").title()
                        student["name"] = edit_name
                        students.sort(key=lambda student: student["name"])
                        
                        print(f"{var_search} has successfully been edited to {edit_name}!!!")                        
                        
                        with open("students.json", "w") as var_file:
                            json.dump(students, var_file, indent = 4)

            elif edit_option == "Age":
                        edit_age = int(input("Enter students proper age: "))
                        student["age"] = edit_age
                        print(f"{student['name']} age has been changed to {student['age']}.")
                        with open("students.json", "w") as var_file:
                            json.dump(students, var_file, indent = 4)
                        
    


    elif option_num == 5:
        var_search = input("Search student name: ").title()
        student_found = False
        matching_students = []

        for student in students:
            if var_search == student["name"]:
                matching_students.append(student)
     
        edit_confirm = "No"
        if len(matching_students) == 0:
            print("Student not found.")

        elif len(matching_students) == 1:
            student = matching_students[0]
            print(f"{student['name']} ({student['Student ID']}) is enrolled in this class.")
            edit_confirm = input("Would you like to edit this student? ").title()

        elif len(matching_students) >= 2:
                print("There are multiple students found:")
                for student in matching_students: 
                    print(f"{student['name']} ({student['Student ID']})")
                ID_specification = int(input("Enter ID of student you are looking for: ")) 
                

                for student in matching_students:
                    if ID_specification == student["Student ID"]:
                        edit_confirm = input("Would you like to edit this student? ").title()   
                        break
                else:
                    print("Student not found.") 


    elif option_num == 6:
        print("You have successfully been logged out.")
        running = False

    else:
        print("Invalid option. Please enter 1, 2, 3, 4, or 5")

