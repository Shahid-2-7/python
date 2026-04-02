def add(a,b,c = 0):
    print(a+b+c)

add(2,2)
add(2,2,2)

#the word polymorphism means 'having many forms'. in context to programing, it is used to use a function with same name but with different 'signatures'

class an():
    def sn(self):
        print("Animals make sound")

class dog(an):
    def sn(self):
        print("Dog Barks")

class bird(an):
    def sn(self):
        print("Birs Sings")

class cat(an):
    def sn(self):
        print("Cat Meows")

a = an()
a.sn() 
a1 = dog()
a1.sn()
a2 = bird()
a2.sn()
a3 = cat()
a3.sn()
