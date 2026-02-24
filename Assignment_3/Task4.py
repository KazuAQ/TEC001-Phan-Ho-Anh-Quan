username = "python"
password = "rules"

count = 0

while count < 5:
    inputname = input("Enter username: ")
    inputpass = input("Enter password: ")
    
    if inputname == username and inputpass == password:
        print("Welcome")
        break
    else:
        count += 1
        if count < 5:
            print("Incorrect username or password. Try again.")
        else:
            print("Access denied")
