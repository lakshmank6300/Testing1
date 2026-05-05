def calculate_price(price, tax,discount):
    total = price + (price * tax)
    return total - discount