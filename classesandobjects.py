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






