def calculate_price(price, tax):
    print("Calculating final price...")
    total = price + (price * tax)
    print(f"Total price is: {total}")
    return total