
class phone():

    ct = "C-Type" #If "C-Type" is same for all objects, to save time we assign this to all objects 

    def __init__(self,brand,price):
        self.brand = brand 
        self.price = price

    def display(self):
        print("Brand name :", self.brand)
        print("Price :", self.price)
        print("Charger Type:", self.ct)

realme = phone("RealMe", "10,000")
oppo = phone("Oppo", "7,500")
apple = phone("Apple IPhone", "1,10,000")

realme.display()
oppo.display()
apple.display()


        