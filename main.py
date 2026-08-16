print("=====================")
print("Student Grade Manager")
print("=====================")

teacher_name = input("What is your name: ").title()
running = True


print()
print(f"Hello {teacher_name}! Welcome to your very own Student Grade Manager!")
print()

with open("students.txt", "r") as var_file:
    students = var_file.readlines()
    
    clean_students = []

    for student in students:
        clean_students.append(student.strip())

    students = clean_students
        
while running:
    print("1. Add student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Search for student")
    print("5. Exit")
    print()

    option_num = int(input("What would you like to do? "))

    if option_num == 1:
        added_student = input("Student name: ").title()
        students.append(added_student)
        students.sort()
        
        with open("students.txt", "w") as var_file:
            for student in students:
                var_file.write(student + "\n")

        
        print(f"{added_student} has been added to your class!")

    elif option_num == 2:
        print("----------------")
        print(f"{teacher_name}'s Class List!")
        print("----------------")
        
        for student in students:
            print(student)
            print()
    
        del student
        
    elif option_num == 3:
        var_remove = input("Enter full student name: ").title()
        var_confirmation = input("Are you sure you'd like to remove this student and all their data? ").title()

        if var_confirmation == "Yes":
            if var_remove in students:
                students.remove(var_remove)
                print(f"{var_remove} has been removed from your class.")

                with open("students.txt", "w") as var_file:
                    for student in students:
                        var_file.write(student + "\n")
               
            else:
                print("Student does not exist.")


    elif option_num == 4:
        var_search = input("Search student name: ").title()
        
        if var_search in students:
            print(f"{var_search} is enrolled in this class.")
            edit_confirm = input("Would you like to edit this student? ").title()

            if edit_confirm == "Yes":
                edit_student = input("Enter students new name: ").title()
                student_index = students.index(var_search)
                students[student_index] = edit_student
                students.sort()
                print(f"{var_search} has successfully been edited to {edit_student}!!!")

                with open("students.txt", "w") as var_file:
                    for student in students:
                        var_file.write(student + "\n")
        

        else:
            print("Student not found.")


    elif option_num == 5:
        print("You have successfully been logged out.")
        running = False

    else:
        print("Invalid option. Please enter 1, 2, 3, 4, or 5")

