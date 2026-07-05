import bakery_menu
cartTotal = 0
cart = {}
def itemSelection():
    global cartTotal
    while True: 
        try:
            selectItem = int(input("Select => "))
            match selectItem:
                case 1:
                    cartTotal += bakery_menu.bakeryMenu["beverages"]["1 - Black Coffee"]
                    cart["Black Coffee"] = cart.get("Black Coffee", 0) + 1
                case 2:
                    cartTotal += bakery_menu.bakeryMenu["beverages"]["2 - Latte"]
                    cart["Latte"] = cart.get("Latte", 0) + 1
                case 3:
                    cartTotal += bakery_menu.bakeryMenu["beverages"]["3 - Tea"]
                    cart["Tea"] = cart.get("Tea", 0) + 1
                case 4:
                    cartTotal += bakery_menu.bakeryMenu["Food"]["4 - Croissant"]
                    cart["Croissant"] = cart.get("Croissant", 0) + 1
                case 5:
                    cartTotal += bakery_menu.bakeryMenu["Food"]["5 - Muffin"]
                    cart["Muffin"] = cart.get("Muffin", 0) + 1
                case 6:
                    cartTotal += bakery_menu.bakeryMenu["Food"]["6 - Cookie"]
                    cart["Cookie"] = cart.get("Cookie", 0) + 1
                case 7:
                    break
                case _:
                    print("Invalid key given! Try again!")
                    
        except Exception:
            print("Error found! Try again")

