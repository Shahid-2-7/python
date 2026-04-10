pizza_price = 0
def add_base(size):
    global pizza_price
    if size == "S":
        pizza_price += 6
    elif size == "M":
        pizza_price += 8
    elif size == "L":
        pizza_price += 10

def toppings(items):
    global pizza_price
    if items == "P":
        pizza_price += 8
    elif items == "C":
        pizza_price += 8
    elif items == "B":
        pizza_price += 10
    elif items == "M":
        pizza_price += 5

j = True 
while j:
    size = input("Select pizza size (S/M/L)")
    add_base(size.capitalize())
    jj = True
    while jj:
        items = input("Select toppings:(P-Pepperoni, M-Mushroom, C-Chicken, B-Beef)")
        toppings(items.capitalize())
        loop = input("Add another topping? (Y-Yes,Any other key to stop)")
        if loop.capitalize() == "Y":
            continue
        else:
            jj = False
    print(pizza_price)
    j = False




