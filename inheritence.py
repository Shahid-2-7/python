class cpu():
    def intel(self):
        print("Intel CPU")

class ram(cpu):
    def ddr4(self):
        print("DDR4 Ram sticks")

class motherboard(ram):
    def asustek(self):
        print("Asus Mother board")

class pc(motherboard):
    def pcsetup(self):
        print("I Have pc setup")
#chaining 2 classes are called single inheritence.
#chaining 3 or more classes are called multiple in heritence
#if you chained two classes which is connected to another class you can access the command of that one too.
#line 18 is called multi-level inheritence

person = pc()
person.intel()
person.pcsetup()