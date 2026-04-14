import re

def redact(text):
    pattern = r'\+84\d+|(?<!\d)\d{10}(?!\d)'
    return re.sub(pattern, '[REDACTED]', text)