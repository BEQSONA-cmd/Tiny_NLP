from dataset import categories, responses
from tokenize import tokenize

def process_input(user_input):
    tokens = tokenize(user_input)

    for number, category in categories.items():
        if category in tokens:
            return responses[number]

    
    return "Sorry, I don't understand that."