cofpow =1
hfee = 30

def cofpowcmd():
    try:
        cpprice = int(input("Select Shots of Coffee (1/2/3)=>"))
        if cpprice == 1:
            cpprice = cofpow * 8
        elif cpprice == 2:
            cpprice = cofpow *16
        elif cpprice == 3:
            cpprice = cofpow *24
        else:
            print("Unknown input given. Coffee powder shots set to 2. Run program again to customize")
            cpprice = cofpow *16
        return cpprice
    except Exception:
            print("Letters given instead of strings")

def espresso():
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
    cpprice = cofpowcmd()
    tprice = cpprice + wprice + cprice + hfee + sprice
    return tprice
cofpowcmd()
espresso()
tprice = espresso()
print(tprice)

