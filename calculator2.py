
class calculator:

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b 

    def add(self):

        print("Addition result = ", self.num1 + self.num2 )

    def sub(self):

        print("Subraction result = ", self.num1 - self.num2 )

    def mul(self):

        print("Multiplication result = ", self.num1 * self.num2 )

    def div(self):

        print("Divison result = ", self.num1 / self.num2 )
        
object = calculator(8,5) 

object.add()
object.sub()
object.mul()
object.div()





        




