def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return price*(1+(discount_percent/100))
    else:
        return price
    
price = float(input("What's the price of the item: "))
while True:
    discount_input = input("What is your discount percentage (or type 'none' for no discount): ")
    if discount_input.lower() == 'none':
        discount = 0
        break
    try:
        discount = float(discount_input)
        if discount < 0:
            raise ValueError("Discount percentage cannot be negative.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid discount percentage.")



result = calculate_discount(price,discount)
print(result)