import re

def valid_check(course):
    
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(pattern, course))