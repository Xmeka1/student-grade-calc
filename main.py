print("=====================")
print("Student Grade Manager")
print("=====================")

teacher_name = input("What is your name: ")

print()
print(f"Hello {teacher_name}! Welcome to your very own Student Grade Manager!")
print()
print("1. Add student")
print("2. View Students")
print("3. Exit")

students = ["Alex Jr", "Elizabeth Moemeka", "Lebron James"]

option_num = int(input("What would you like to do? "))

if option_num == 1:
    added_student = input("Student name:")
    students.append(added_student)
    print(f"{added_student} has been added to your class!")

elif option_num == 2:
    for student in students:
        print(student)
    

elif option_num == 3:
    print("You have successfully been logged out")

else:
   print("Not an option. Restart program if you wish to try again")

