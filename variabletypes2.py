class laptop:

    chargertype = "B-Type"
    def __init__(self):
        self.price = "???"
        self.brand = ""

    def setprice(self, price):
        self.price = price
        print("Price:", price)
         
    @classmethod
    def display(cls):
        cls.chargertype = "C-Type"
        print("Charger type changed to c-type.")

hp = laptop()
hp.setprice(20000)
laptop.display()




 