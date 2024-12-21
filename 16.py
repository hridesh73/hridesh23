menu = input("Enter item (Pizza, Burger, Pasta): ").capitalize()
prices = {"Pizza": 10, "Burger": 7, "Pasta": 8}
print(f"Price: ${prices.get(menu, 'Invalid item')}")
