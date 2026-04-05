class person():

    def __init__(self, name):
        self.name = name

class student(person):

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

obj = student("Shahid","A")
obj.display()

class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
         print("Name of employee:",self.name)
         print("Salary of employee:",self.salary)
         print("Department of employee:",self.department)
        
        
e1 = manager("shahid", "35,000", "AI Tools development")
e1.display()




