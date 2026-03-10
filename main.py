a = input("Enter student name: ")
b = input("Food choices: 1- Raw Liver, 2- Steak Tartare, 3- Sashimi: ")


if b == '1' :
    price = 12
    food = "Raw Liver"
elif b == '2' :
    price = 8
    food = "Steak Tartare"
elif b == '3' :
    price = 5
    food = "Sashimi"
else:
    price = 0
    food = "Invalid"


discount = 0
if price > 10:
    discount = 2

final_price = price - discount


print("\n----- RECEIPT -----")
print(f"Student: {a}")
print(f"Food: {food}")
print(f"Base Price: ${price}")
if discount > 0:
    print(f"Discount: -${discount}")
print(f"Total: ${final_price}")
