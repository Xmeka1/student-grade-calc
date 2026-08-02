print("=====================")
print("Student Grade Manager")
print("=====================")

teacher_name = input("What is your name: ").title()
running = True
students = ["Alex Jr", "Elizabeth Moemeka", "Lebron James"]

print()
print(f"Hello {teacher_name}! Welcome to your very own Student Grade Manager!")
print()
while running:
    print("1. Add student")
    print("2. View Students")
    print("3. Exit")
    print()

    option_num = int(input("What would you like to do? "))

    if option_num == 1:
        added_student = input("Student name: ").title()
        students.append(added_student)
        students.sort()
        
        print(f"{added_student} has been added to your class!")

    elif option_num == 2:
        print("----------------")
        print(f"{teacher_name}'s Class List!")
        print("----------------")
        
        for student in students:
            print(student)
    

    elif option_num == 3:
        print("You have successfully been logged out")
        running = False

    else:
        print("Invalid option. Please enter 1, 2, or 3")

