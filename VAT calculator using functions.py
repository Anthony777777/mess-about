def importVAT(price, isDocument):
    # This is a function that calculates import VAT
    if isDocument == "yes":
        new_price = price
    else:
        new_price = price * 1.2
    return new_price

# This is a program that calculates the final price of an imported item
price = float(input("Please enter the price of your item: "))
# Check if the item is a document. The user can simply enter yes or no
isDocument = input("Is your item a book or magazine? (yes/no)")

final_price = importVAT(price, isDocument) # this is a function call

print("The final price you need to pay for your item is: ",final_price)