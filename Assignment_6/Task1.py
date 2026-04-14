nums = []

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break
    try:
        nums.append(float(num))
    except:
        print("Please enter a valid number.")

nums.sort(reverse=True)
top_five = nums[:5]

print("Five greatest numbers in descending order:")
print(top_five)