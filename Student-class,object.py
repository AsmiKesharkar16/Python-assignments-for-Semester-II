class Student:
    def __init__(self, student_name, roll_no, maths, physics, chemistry, total, average):
        self.student_name = student_name
        self.roll_no = roll_no
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.total = total
        self.average = average

    def accept_details(self): 
        self.student_name=input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.maths = float(input("Enter marks out of 100 for following subjects:\nEnter marks in Maths: "))
        self.physics = float(input("Enter marks in Physics: "))
        self.chemistry = float(input("Enter marks in Chemistry: "))

    def calculate(self):
        self.total= self.maths+self.physics+self.chemistry
        self.average= self.total/3

    def display_info(self):
        print("\nSTUDENT DETAILS:-")
        print("---------------------------------------------")
        print("Student Name:", self.student_name)
        print("Roll Number:", self.roll_no)
        print("Maths:", self.maths)
        print("Physics:", self.physics)
        print("Chemistry:", self.chemistry)
        print("Total Marks out of 300:", self.total)
        print("Average Marks:", self.average)
        print("---------------------------------------------")

student=Student("","","","","","","")
student.accept_details()
student.calculate()
student.display_info()