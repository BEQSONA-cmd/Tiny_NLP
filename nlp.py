from dataset import responses
from tokenize import tokenize

def process_input(user_input):
    tokens = tokenize(user_input)
    
    for phrase in responses:
        if all(word in tokens for word in phrase.split()):
            return responses[phrase]
    
    return "Sorry, I don't understand that."