bakeryMenu = {
    "beverages" : {
        "1 - Black Coffee" : 2.5,
        "2 - Latte" : 3.75,
        "3 - Tea" : 2
    },
    "Food" : {
        "4 - Croissant" : 3,
        "5 - Muffin" : 2.75,
        "6 - Cookie" : 1.5
    }
}

def showMenu():
    for i , j in bakeryMenu.items():
        print(i,":",j,)
    print("7 - Exit")
