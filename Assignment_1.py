import math
import random

'''2. Write a program that asks your name and then greets you by your name. Example:
If you enter Mai as your name, the program will greet you with Hello, Mai!.'''

name=str(input("Enter Your name: "))
print("Hello, "+name)

"""3. Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle."""

radius=int(input("Enter radius: "))
print(f"Circumferance of the circle: {2*radius*math.pi}")

"""4. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides."""

length=int(input("Enter length: "))
width=int(input("Enter width: "))

print(f"Rectangle's perimeter: {2*(length+width)}")
print(f"Area of the rectangle: {length*width}")

"""5. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers."""

a,b,c=map(int, input("Enter 3 intergers with spaces between them: ").split())
print(f"Sum: {a+b+c}")
print(f"Product: {a*b*c}")
print(f"Average: {(a+b+c)/3}")

"""Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots. The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams."""

talent=int(input("Enter talents: "))
pound=int(input("Enter pounds: "))
lot=int(input("Enter lots: "))

print(f"{((talent*20*32*13.3)+(pound*32*13.3)+(lot*13.3))//1000} kilograms and {int(((talent*20*32*13.3)+(pound*32*13.3)+(lot*13.3))%1000)} grams")

"""7. Write a program that draws two random combinations of numbers for a combination lock:

a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6."""

print(f"3-digit code: {random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
print(f"4-digit code: {random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}")