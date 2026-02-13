class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("------------------------------------------")

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
 
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department): 
        Person.__init__(self, name, age) 
        Employee.__init__(self, employee_id, salary) 
        self.department = department 

    def display_manager_info(self):
        print("Department:", self.department) 

    def display_full_info(self): 
        print("------------------------------------------")
        print(self.name,"is managing the",self.department,"department.")
        print("------------------------------------------")

m = Manager("Asmi", 25, "B0261", 200000, "CSE")
m.display_person_info()
m.display_employee_info()
m.display_manager_info()
m.display_full_info()
