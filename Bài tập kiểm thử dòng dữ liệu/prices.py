def price_calculator(amount: int, price: int):
    if price < 0 | amount < 0:
        return 0
    total = 0
    if amount < 5:
        total = price * amount
    elif amount < 10:
        total = price * amount * 0.95
    else:
        total = price * amount * 0.90
    return total