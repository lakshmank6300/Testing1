def calculate_price(price, tax,discount):
    total = price + (price * tax)
    return total - discount
    print("Calculating final price...")
    tax_amount = price * tax
    total = price + tax_amount
    final_price = total-discount
    print(f"Final price is: {final_price}")
    return round(final_price, 2)
