meal_input = input("How much was the meal? ")
percent_input = input("What percentage would you like to tip? ")

dollars = float(meal_input.replace("$", ""))
percent = float(percent_input.replace("%", "")) / 100

tip = dollars * percent

print(f"Leave ${tip:.2f}")