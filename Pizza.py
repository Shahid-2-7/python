prices = {
    "pizza_price" : 0,
    "s" : 5,
    "m" : 8,
    "l" : 10,
    "pepperoni" : 5,
    "chicken" : 8,
    "beef" : 10,
    "mushroom":5,
    "thin_crust" : 5,
    "normal" : 7,
    "cheese_burst" : 9,
}
def pizza_size(size):
    if size == "S":
        prices["pizza_price"] += prices["s"]
    elif size == "M":
        prices["pizza_price"] += prices["m"]
    elif size == "L":
        prices["pizza_price"] += prices["l"]
    else:
        pass #print (invalid input) and retry
def toppings(topping):
    if topping == "P":
        prices["pizza_price"] += prices["pepperoni"]
    elif topping == "C":
        prices["pizza_price"] += prices["chicken"]
    elif topping == "B":
        prices["pizza_price"] += prices["beef"]
    elif topping == "M":
        prices["pizza_price"] += prices["mushroom"]
    else:
        pass #print (invalid input) and retry
while True:
    size = input("select pizza size =>")
    if size.capitalize() == "S" or size.capitalize() == "M" or size.capitalize() == "L":
        pizza_size(size.capitalize())
    else:
        print("Try again")
        continue #function la if else irunthaa pothum dont use it here (just call the function the validations are done inside the function not here)
    while True:
        topping = input("select topping (P-Pepperoni, C-Chicken, B-Beef, M-Mushroom) =>")
        if topping.capitalize() == "P" or topping.capitalize() == "C" or topping.capitalize() == "B" or topping.capitalize() == "M":
            toppings(topping.capitalize())
            add = input("Add another topping? (Y-Yes, any other key-No)")
            if add.capitalize() == "Y":
                continue
            else:
                break
        else:
            print("Try again")
            continue
    print(f"Total =>{prices["pizza_price"]}")
    payment = int(input("1-Cash, 2-Card"))
    if payment == 1:
        notes = int(input("Cash =>"))
        coins = float(input("Coins =>"))
        if coins + notes == prices["pizza_price"]:
            print("Payment successful!")
            break
        elif coins + notes > prices["pizza_price"]:
            print(f"Heres your change =>{(notes+coins) -prices["pizza_price"]}")
            break
        elif notes + coins < prices["pizza_price"]:
            print("Not enough money, Try again")
            continue
    elif payment == 2:
        print("Swipe card")
        print("payment successful!")
        break

        


        
