cofpow = 1
milk = 0.0065
sugar = 0.045
hfee = 20

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

def latte():
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
    cpprice = cofpowcmd()
    tprice = cpprice + cprice + hfee + sprice + mprice
    return tprice

def cappuccino():
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
    cpprice = cofpowcmd()
    tprice = cpprice + mprice + cprice + hfee + sprice
    return tprice
    
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

j = True 
while j:
    coffeetype = input("What would you like to have to today?(E-Espresso C-Cappuccino L-Latte)")
    if coffeetype.capitalize() == "E":
        cofpowcmd()
        espresso()
        tprice = espresso()
        print(f"Total {tprice}.")
        j = False
        
    elif coffeetype.capitalize() == "C":
        cofpowcmd()
        cappuccino()
        tprice = cappuccino()
        print(f"Total {tprice}.")
    elif coffeetype.capitalize() == "L":
        cofpowcmd()
        latte()
        tprice = latte()
        print(f"Total {tprice}.")
    else:
        continue


    


