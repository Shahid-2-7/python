cofpow = 1
milk = 0.0065
sugar = 0.045
hfee = 20

def cofpowcmd(shots):
    try:
        if shots == 1:
            cpprice = cofpow * 8
        elif shots == 2:
            cpprice = cofpow *16
        elif shots == 3:
            cpprice = cofpow *24
        else:
            print("Unknown input given. Coffee powder shots set to 2. Run program again to customize")
            cpprice = cofpow *16
        return cpprice
    except Exception:
            print("Letters given instead of strings")
            return 0

def latte(shots):
    cupsize = input("Select Size (S - 30ml, M - 60ml, L - 90ml)=>")
    if cupsize.capitalize() == "S":
        print("size small cup is taken to serve!")
        cprice = 3.5
        sprice = 0.23 * 1.5
        mprice = milk * 25
    elif cupsize.capitalize() == "M":
        print("size medium cup is taken to serve!")  
        cprice = 4.5
        sprice = 0.23 * 3
        mprice = milk * 50
    elif cupsize.capitalize() == "L":
        print("size large cup is taken to serve!")
        cprice = 6
        sprice = 0.23 * 4.5
        mprice = milk * 75       
    else:
        print("Unknown input given. Run program again for proper working of the machine")
    cpprice = cofpowcmd(shots)
    tprice = cpprice + cprice + hfee + sprice + mprice
    return tprice

def cappuccino(shots):
    cupsize = input("Select Size (S-30ml, M-60ml, L-90ml)=>")
    if cupsize.capitalize() == "S":
        print("size small cup is taken to serve!")
        cprice = 3.5
        mprice = milk * 20
        sprice = 0.23 
    elif cupsize.capitalize() == "M":
        print("size medium cup is taken to serve!")
        cprice = 4.5
        mprice = milk * 40
        sprice = 0.23 * 2
    elif cupsize.capitalize() == "L":
        print("size large cup is taken to serve!")
        cprice = 6
        mprice = milk * 60
        sprice = 0.23 * 3    
    else:
        print("Try Again")
    cpprice = cofpowcmd(shots)
    tprice = cpprice + mprice + cprice + hfee + sprice
    return tprice
    
def espresso(shots):
    cupsize = input("Select Size (S-30ml, M-60ml, L-90ml)=>")
    if cupsize.capitalize() == "S":
        print("size small cup is taken to serve!")
        cprice = 3.5
        wprice = 2
        sprice = 0.23
    elif cupsize.capitalize() == "M":
        print("size medium cup is taken to serve!")
        cprice = 4.5
        wprice = 4
        sprice = 0.23
    elif cupsize.capitalize() == "L":
        print("size large cup is taken to serve!")
        cprice = 6
        wprice = 6
        sprice = 0.36         
    else:
        print("Unknown input given. Run program again for proper working of the machine")
    cpprice = cofpowcmd(shots)
    tprice = cpprice + wprice + cprice + hfee + sprice
    return tprice

j = True 
while j:
    coffeetype = input("What would you like to have to today?(E-Espresso C-Cappuccino L-Latte)")
    shots = int(input("Select Shots of Coffee (1/2/3)=>"))

    if coffeetype.capitalize() == "E":
        tprice = espresso(shots)
        print(f"Total {tprice}.")

    elif coffeetype.capitalize() == "C":
        tprice = cappuccino(shots)
        print(f"Total {tprice}.")

    elif coffeetype.capitalize() == "L":
        tprice = latte(shots)
        print(f"Total {tprice}.")
    


    


