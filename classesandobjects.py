class student:

    def __init__ (self):
        self.NameOfStd = "Student didnt register his name"
        self.regnum = "Student didnt register his register number"

    def display(self):
        print("Name: ", self.NameOfStd)
        print("Register Number: ", self.regnum)

S1 = student()
S2 = student()

print(S1.NameOfStd)
print(S2.NameOfStd)
print(S1.regnum)
print(S2.regnum)

S1.NameOfStd = "Shahid"
S2.NameOfStd = "Anwershah"
S1.regnum = "5237"
S2.regnum = "6218"

print(S1.NameOfStd)
print(S2.NameOfStd)
print(S1.regnum)
print(S2.regnum)

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

print(apple.colour, orange.colour, kiwi.colour, papaya.colour, end = "")
