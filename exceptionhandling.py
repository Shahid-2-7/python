#exception is known as error
#exception handling has three types:
# 1. compile time error happens when editor is reading line by line(compiling) and finds mistake
# 2. logical errors most of the time it successfully executes the program but it is actually logically wrong like this:
a = 10
b = 20
print(a+a) #here it should be print(a+b), so technically this correct but logically it is'nt
# 3. run time error happens when program is completely fine but the user messes it up and it detects an error.
# if you dont want the program to throw an error you could end the program successfully with an error 
try:
    a = int(input("num 1: "))
    b = int(input("num 2: "))
    c = int(input("num 3: "))
    print(a+b-c)

except Exception as e:
    print("(===>!ERROR!<===):", e)

finally:
    print("user input is correct")



