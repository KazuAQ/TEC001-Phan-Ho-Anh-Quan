def get_acro(string):
    words = string.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym
string=str(input("Enter a phrase: "))
print(get_acro(string))
