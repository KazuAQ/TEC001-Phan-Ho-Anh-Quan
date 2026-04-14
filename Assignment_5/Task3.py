import re

def sum(text):
    numbers = re.findall(r'\d+', text)
    return sum(int(num) for num in numbers)