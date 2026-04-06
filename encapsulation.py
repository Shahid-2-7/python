class a():
    def __init__(self):
        self.__cname = "google"

    def dis(self):
        print(self.__cname)

o1 = a()
o1.dis()
 #'__' make a variable uncustomizable outside the class. 
 #if you try to edit it outside the class, it will show an error that the class doesnt have that attribute


