def total_cost(prices):
    total = sum(prices)

    if total > 1000:
        total *= 0.90 

    total *= 1.08

    return round(total, 2)


items = [120, 300, 420, 400]
final_amount = total_cost(items)
print("final price is: Rs", final_amount)