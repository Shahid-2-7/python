class student:

    def __init__ (self): 

        self.NameOfStd = "Student didnt register his name"
        self.regnum = "Student didnt register his register number"

    def display(self):

        print("Name: ", self.NameOfStd)
        print("Register Number: ", self.regnum)

S1 = student()
S2 = student()

S1.NameOfStd = "Shahid"
S2.NameOfStd = "Anwershah"
S1.regnum = "5237"
S2.regnum = "6218"

S1.display()
S2.display()

#below example explains a different method of changing values for objects in a class:

class fruit:

    def __init__(self, col):
        self.colour = col
        
apple = fruit("red")
orange = fruit("orange")
kiwi = fruit("green")
papaya = fruit("yellow")

print(apple.colour, orange.colour, kiwi.colour, papaya.colour)

class teacher:

    def __init__ (self, m, n):
        self.tname = m
        self.treg = n
    def disteach(self):
        print("name: ", self.tname)
        print("register number: ", self.treg)

bala = teacher("Bala", 6543)
surya = teacher("Surya", 4328)

bala.disteach()
surya.disteach()



    
