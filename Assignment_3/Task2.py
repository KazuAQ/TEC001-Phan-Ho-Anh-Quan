while True:
    inch = float(input("Enter inches (negative value to exit): "))
    
    if inch < 0:
        break
    
    cm = inch * 2.54
    print(f"{inch} inches = {cm} centimeters\n")

print("Program ended.")
