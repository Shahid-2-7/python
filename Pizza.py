# size -> pizza size (S/M/L)
# l = 10
# m = 8
# s = 6

# crust -> thin crust, thick crust, cheese burst, normal
# normal = 0
# thin_crust = +5
# thick_crust = +7
# cheese_burst = +10


# topping -> [list of available toppings]
#     mushroom -> continue or another topping

# mushroom = 5
# chicken = 10
# pepporoni = 8

pizza_price = 0

L_price = 10
M_price = 8
S_price = 6

normal = 0
thin_crust = 5
thick_crust = 7
cheese_burst = 10

mushroom = 5
chicken = 10
pepporoni = 8

def add_base(size):
    global pizza_price
    if size == "L":
        pizza_price += L_price
    elif size == "M":
        pizza_price += M_price
    elif size == "S":
        pizza_price += S_price

size = input("Enter pizza size (S/M/L): ")
add_base(size.capitalize())
# code below

# crust function




# toppings function


# code above
print(pizza_price)