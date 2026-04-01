class laptop:

    chargertype = "B-Type"
    def __init__(self):
        self.price = "???"
        self.brand = ""

    def setprice(self, price): #this is instance method
        self.price = price
        print("Price:", price)

    @classmethod  #this is called decoraters this one is used to call a function in a class with the class itself
    #above is called class method
    def display(cls):
        cls.chargertype = "C-Type"
        print("Charger type changed to c-type.")

    @staticmethod  #this decorater is used to access a function without keyword self
    #above is called static method
    def information():
        print("Class = laptop")

hp = laptop()
hp.setprice(20000)
laptop.display()
hp.information()




 