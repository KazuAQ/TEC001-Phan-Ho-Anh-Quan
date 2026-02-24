import math
num = int(input("Enter an integer: "))
while True:
    if num < 2:
        print(f"{num} is not a prime number.")
        break
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
            else:
                print(f"{num} is a prime number.")