item = input("Is your item a Book or a Document? " )
price = float(input("How much is your Item? "))
overseas = input("Is your item from overseas? ")
VAT = (20 * price)/100
if item == "yes":
    if overseas == "yes":
        print("Total price: ",  price)
if item == "no":
    if overseas == "yes":
        print("Total price: ", VAT + price)
    else: print("Total price: ", price)