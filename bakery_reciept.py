import bakery_cart
def receiptPrint():
    print("=====RECEIPT=====")
    for item,count in bakery_cart.cart.items():
        print(count,"X",item)
    print("Grand Total =", bakery_cart.cartTotal,"$")
