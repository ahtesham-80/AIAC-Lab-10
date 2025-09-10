def discount(price, category):
    if category == "student":
        return price * (0.9 if price > 1000 else 0.95)
    return price * 0.85 if price > 2000 else price
print(discount(1000, "student"))
print(discount(1000, "adult"))
print(discount(1000, "senior"))
print(discount(1000, "child"))


