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

person = pc()
person.asustek()
person.ddr4()
person.intel()
person.pcsetup()