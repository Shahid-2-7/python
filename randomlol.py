def function():
    yield 1
    yield 2
    yield 3

obj = function()
print(next(obj))





