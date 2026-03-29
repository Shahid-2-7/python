aa = []
run = True
while run == True:
    value1 = int(input("enter number for first value: "))
    value2 = int(input("enter number for second value: "))
    mc = int(input("type 1 to add 2 to subtract 3 to multiply and 4 to divide. "))
    a = 0
    match mc:
        case 1:
            a = value1 + value2 
            print("Result =", a)
            # aa.append(a)
        case 2:
            a = value1 - value2 
            print("Result =", a)
            # aa.append(a)
        case 3:
            a = value1 * value2 
            print("Result=", a)
            # aa.append(a)
        case 4:
            a = value1 / value2 
            print("Result=", a)
            # aa.append(a)
        case _:
            print("Ivalid key!")
            
    # if mc == 1 :
        
    #     a = value1 + value2 
    #     print("Result =", a)
    #     aa.append(a)    

    # elif mc == 2:
        
    #     a = value1 - value2 
    #     print("Result =", a)
    #     aa.append(a)
    # elif mc == 3 :
       
    #     a = value1 * value2 
    #     print("Result=", a)
    #     aa.append(a)

    # elif mc == 4 :
    #     a = value1 / value2 
    #     print("Result=", a)
    #     aa.append(a)

    # else :
    #     print("!INVALID MATHEMATIC OPERATION!")
    aa.append(a)
    m = input("Press Y for redo, N for Showing history and end the calculation : ")
    
    if m.capitalize() == 'N': #n -> N, N -> N
        print(aa)
        run = False
    else:
        continue




