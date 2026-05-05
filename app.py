def calculate_price(price, tax):
    tax_amount = price * tax
    total = price + tax_amount
    return round(total, 2)