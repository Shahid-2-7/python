cofpow = 1
milk = 0.0065
sugar = 0.045
hfee = 20

j = True

while(j):

    try:
        coffeetype = input("What would you like to have today? (L - Latte, C - Cappuccino, E - Espresso)=> ")

        if coffeetype.capitalize() == "L":
            
            try:
                cpprice = int(input("Select Shots of Coffee (1/2/3)=>"))

                if cpprice == 1:
                    cpprice = cofpow * 8

                elif cpprice == 2:
                    cpprice = cofpow *16

                elif cpprice == 3:
                    cpprice = cofpow *24

                else:
                    print("Try Again")
                    continue

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
                    print("Try Again")
                    continue
                
                tprice = cpprice + cprice + hfee + sprice + mprice

                payment = input(f"your total is => {tprice} C - Cash or O - One Time Code for payment?=>")

                if payment.capitalize() == "C":
                    cash = int(input("Cash: "))
                    coins = float(input ("Coins: "))

                    if cash + coins > tprice:
                        print(f"Heres your Change =>{tprice - (cash + coins)}")

                    elif cash + coins == tprice:
                        process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N - No)=>")

                        if process.capitalize()== "Y":
                            print("Getting prepared for the next order...")
                        
                        elif process.capitalize()== "N":
                            j = False
                    
                    else:
                        ("Insufficient Money recieved: Missing some money")
                        continue
                
                if payment .capitalize() == "O":
                    print("One Time Code: 84937")
                    process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N - No)=>")

                    if process.capitalize()== "Y":
                        print("Getting prepared for the next order...")
                        
                    elif process.capitalize()== "N":
                        j = False
                
            except Exception as e:
                print("ERROR:", e)

        elif coffeetype.capitalize() == "C":
            
            try:
                cpprice = int(input("Select Shots of Coffee (1/2/3)=>"))

                if cpprice == 1:
                    cpprice = cofpow * 8

                elif cpprice == 2:
                    cpprice = cofpow *16

                elif cpprice == 3:
                    cpprice = cofpow *24

                else:
                    print("Try Again")
                    continue

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
                    continue

                tprice = cpprice + mprice + cprice + hfee + sprice

                payment = input(f"your total is => {tprice} C - Cash or O - One Time Code for payment?=>")

                if payment.capitalize() == "C":
                    cash = int(input("Cash: "))
                    coins = float(input ("Coins: "))

                    if cash + coins > tprice:
                        print(f"Heres your Change =>{tprice - (cash + coins)}")
                        
                    if cash + coins == tprice:
                        process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N - No)=>")
                        
                        if process.capitalize()== "Y":
                            print("Getting prepared for the next order...")
                        
                        elif process.capitalize()== "N":
                            j = False

                        else:
                            print("Insufficient Money recieved: Missing some money")
                            continue

                elif payment .capitalize() == "O":
                    print("One Time Code: 84937")
                    process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N - No)=>")
                    if process.capitalize()== "Y":
                        print("Getting prepared for the next order...")
                        
                    elif process.capitalize()== "N":
                        j = False

            except Exception as e:
                print("ERROR:", e)
            
        elif coffeetype.capitalize() == "E":

            try:
                cpprice = int(input("Select Shots of Coffee (1/2/3)=>"))

                if cpprice == 1:
                    cpprice = cofpow * 8

                elif cpprice == 2:
                    cpprice = cofpow *16

                elif cpprice == 3:
                    cpprice = cofpow *24

                else:
                    print("Try Again")
                    continue

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
                    print("Try Again")
                    continue

                tprice = cpprice + wprice + cprice + hfee + sprice  

                payment = input(f"your total is => {tprice} C - Cash or O - One TIme Code for payment?=>")

                if payment.capitalize() == "C":
                    cash = int(input("Cash: "))
                    coins = float(input ("Coins: "))

                    if cash + coins > tprice:
                        print(f"Heres your Change =>{tprice - (cash + coins)}")
                        
                    if cash + coins == tprice:
                        process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N-No)=>")
                        if process.capitalize()== "Y":
                            print("Getting prepared for the next order...")
                        
                        elif process.capitalize()== "N":
                            j = False

                        else:
                            print("Insufficient Money recieved: Missing some money")
                            continue
                        
                if payment.capitalize() == "O":
                    print("One Time Code: 84937")
                    process = input("Transaction successful, want to buy another drink or stop the process?)(Y - yes, N - No)=>")
                    if process.capitalize()== "Y":
                        print("Getting prepared for the next order...")
                        
                    elif process.capitalize()== "N":
                        j = False

                
            except Exception as e:
                print("ERROR:", e)

           
    except Exception as e:
        print("ERROR:", e)

