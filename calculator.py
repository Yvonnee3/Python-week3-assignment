def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1-discount_percent / 100)
        return discounted_price
    else:
        return price
 
price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discout percentage:   "))

final_price = calculate_discount(price, discount_percentage)

if discount_percentage >= 20:
    print(f"Final price aftet {discount_percentage}% discount : {final_price:.2f}")
else:
    print(f"No discount applied.Original price: {price:.2f}")




