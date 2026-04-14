seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")

month = int(input("Enter a month number (1-12): "))

if 1 <= month <= 12:
    season = seasons[month - 1]
    print(f"Month {month} is in {season}.")
else:
    print("Invalid input. Please enter a number between 1 and 12.")