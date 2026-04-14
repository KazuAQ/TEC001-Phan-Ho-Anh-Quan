import re

def valid_check(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))