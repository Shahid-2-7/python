def add():
    print("addition:")

    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print(a + b)

def subtract():
    print("subtraction:")
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print(a - b)

def multiply():
    print("multiplication:")
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print(a * b)

def divide():
    print("division:")
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print(a / b)

add()
subtract()
multiply()
divide()

def findevenorodd():
    a = int(input("enter number to check if its even or odd: "))
    if a % 2 == 0:
        print("Its even")
    else:
        print("Its odd")

findevenorodd()

def printrange():
    ok = int(input("Enter a number to print range: "))
    for i in range(1,ok + 1):
        print(i, end = ",")

printrange()
