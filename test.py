def func(*args): # '*' makes a variable store multiple values as a tuple
    print(*args) #Unpack the tuple

func(1,2,3,4,5,6,7,8,9,10)

def func2():
    yield 1 #pauses the program and resumes when we ask to do so
    yield 2
    yield 3

a = func2()
print(next(a))
print(next(a))
print(next(a))

def func3():
    return 123

print(func3())
        

