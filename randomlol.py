class person():

    def __init__(self,name):
        self.name = name

class student(person):

    def __init__(self,grade):
        a = input("Enter name: ")
        super().__init__(a)
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)

obj = student("A")
obj.display()



