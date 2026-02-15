import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    area_square_meters = area / 10000
    unit_price = price / area_square_meters
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (USD): "))

diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (USD): "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

print(f"Unit price of the first pizza: ${unit_price1:.2f} per square meter")
print(f"Unit price of the second pizza: ${unit_price2:.2f} per square meter")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price1 > unit_price2:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")