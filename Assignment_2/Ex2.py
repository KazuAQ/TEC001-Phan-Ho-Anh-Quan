Class = input('Please enter your class (LUX, A, B, C)): ')

def classcheck():
    if Class.upper()=='LUX':
        return 'upper-deck cabin with a balcony.'
    elif Class.upper()=='A':
        return 'above the car deck, equipped with a window.'
    elif Class.upper()=='B':
        return 'windowless cabin above the car deck.'
    elif Class.upper()=='C':
        return 'windowless cabin below the car deck.'
    else:
        return 'Invalid cabin class'
    
print(classcheck())
