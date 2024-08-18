import re

def tokenize(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens