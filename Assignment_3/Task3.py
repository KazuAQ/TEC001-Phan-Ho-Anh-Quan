num = []

while True:
    userin = input("Enter a number (or press Enter to quit): ")
    
    if userin == "":
        break
    
    try:
        num = float(userin)
        num.append(num)
    except:
        print("Invalid input. Please enter a valid number.")

if num:
    print(f"Smallest number: {min(num)}")
    print(f"Largest number: {max(num)}")
else:
    print("Ended")
