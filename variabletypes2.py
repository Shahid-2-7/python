class laptop:

    chargertype = "B-Type"
    def __init__(self):
        self.price = "???"
        self.brand = ""

    def setprice(self, price):
        self.price = price
        print("Price:", price)
         
    @classmethod  #this is called decoraters this one is used to call a function in a class with the class itself
    def display(cls):
        cls.chargertype = "C-Type"
        print("Charger type changed to c-type.")

    @staticmethod  #this decorater is used to access a function without keyword self
    def information():
        print("Class = laptop")

hp = laptop()
hp.setprice(20000)
laptop.display()
hp.information()




 