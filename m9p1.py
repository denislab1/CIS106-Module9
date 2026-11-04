
def calculate_total(qty, price):
    total = qty * price

    if total > 10000:
        total = total * 0.90

    return total


grand_total = 0

while True:
    qty = int(input("Enter quantity (0 to stop): "))

    if qty == 0:
        break

    price = float(input("Enter unit price: "))

    total = calculate_total(qty, price)

    print("Quantity:", qty)
    print("Unit price: $", format(price, ".2f"))
    print("Extended price: $", format(total, ".2f"))
    print()

    grand_total = grand_total + total


print("Total extended price: $", format(grand_total, ".2f"))