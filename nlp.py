import random
import logging
from dataset import categories, responses
from tokenize import tokenize

class ChatbotContext:
    def __init__(self):
        self.last_category = None
        self.previous_input = None
        self.follow_up_category = None

    def update_context(self, detected_category, user_input):
        self.last_category = detected_category
        self.previous_input = user_input

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
                logging.info(f"Pattern matched: '{keyword}' in category '{category}'")
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
            logging.info(f"Tokens after tokenization: {tokens}")
            for number, category in categories.items():
                if category in tokens:
                    detected_category = number
                    break

        if detected_category is None:
            detected_category = context.last_category

        if detected_category is None:
            logging.warning(f"No category detected for input: {user_input}")
            return "Sorry, I don't understand that."

        context.update_context(detected_category, user_input)

        if categories.get(detected_category) == 'thanks':
            context.follow_up_category = 'follow_up_thanks'
            return random.choice(responses[detected_category]) + " Is there anything else I can help you with?"

        if detected_category in responses:
            response = random.choice(responses[detected_category])
            logging.info(f"Response selected: {response}")
            return response
        else:
            logging.warning(f"No response available for category: {detected_category}")
            return "Sorry, I don't have a response for that."
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"
