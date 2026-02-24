def get_mid(s):
    length = len(s)
    
    if length == 0:
        return ""
    
    mid = length // 2
    
    if length % 2 == 1:  # Odd length
        return s[mid]
    else:  # Even length
        return s[mid - 1:mid + 1]

s=str(input("Enter a string: "))
print(get_mid(s))
