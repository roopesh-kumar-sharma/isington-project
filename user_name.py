print("Welcome to the College")
student=[]
student_visit="y"
while student_visit=="y":
    Fname=input("Enter the First name of Student : ").capitalize()
    Lname = input("Enter the Last name of Student : ").capitalize()
    Full_name=Fname + " " + Lname
    student.append(Full_name)
    student_visit=input("type y to continue and n to exit : ").lower()
    if student_visit=="n":
        print('')
print("The names of students visiting collge")
for name in student:
    print(name)

