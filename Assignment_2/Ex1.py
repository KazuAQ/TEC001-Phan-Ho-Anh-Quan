import math

def zandercheck():
    length=float(input("Enter zander's length in centimeter: "))
    if length>=42:
        return "You're good to go"
    else:
        return f"Your zander is {42-length}cm below the size limit, please release the fish back into the lake"
    
print(zandercheck())