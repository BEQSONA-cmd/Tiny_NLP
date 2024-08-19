import random
from dataset import categories, responses
from tokenize import tokenize

class ChatbotContext:
    def __init__(self):
        self.last_category = None

context = ChatbotContext()

def pattern_matching(user_input):
    user_input = user_input.lower()

    patterns = {
        'greeting': ['hello', 'hi', 'hey', 'greetings'],
        'goodbye': ['bye', 'goodbye', 'see you', 'farewell'],
    }

    for category, keywords in patterns.items():
        for keyword in keywords:
            if keyword in user_input:
                for number, cat in categories.items():
                    if cat == category:
                        return number

    return None

def process_input_with_pattern(user_input):
    if not user_input.strip():
        return "Please enter a valid message."

    try:
        detected_category = pattern_matching(user_input)
        
        if detected_category is None:
            tokens = tokenize(user_input)
            for number, category in categories.items():
                if category in tokens:
                    detected_category = number
                    break

        if detected_category is None:
            detected_category = context.last_category

        if detected_category is None:
            return "Sorry, I don't understand that."

        context.last_category = detected_category

        if detected_category in responses:
            return random.choice(responses[detected_category])
        else:
            return "Sorry, I don't have a response for that."
    except Exception as e:
        return f"An error occurred: {str(e)}"