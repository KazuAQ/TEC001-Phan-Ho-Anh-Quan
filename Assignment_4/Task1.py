num_list=[]

while True:
    userin=input("Enter a number (enter blank space to exit): ")
    if userin == " ":
        break
    try:
        num=int(userin)
        num_list.append(num)
    except:
        print("Invalid input type")

num_list.sort(reverse=True)
print(num_list)