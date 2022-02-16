from datetime import datetime
import StudentClass as s

def main():
    id = input("What is your student ID?")
    dob= int(input("What year were you born?"))
    name = input("What is your name?")
    classif = input("What is your classification?")

    student1 = s.Student(id,name,dob,classif)
    student1.age()
    print("The student's age is:", student1.get_age())

    student1.registration()
main()