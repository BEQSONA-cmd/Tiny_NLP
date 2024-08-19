import logging
from nlp import process_input_with_pattern

logging.basicConfig(filename='chatbot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def chatbot():
    logging.info("Chatbot started.")
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            logging.info("User ended the conversation with 'bye'.")
            break
        
        logging.info(f"User input: {user_input}")
        
        response = process_input_with_pattern(user_input)
        print(f"Chatbot: {response}")
        
        logging.info(f"Chatbot response: {response}")

if __name__ == "__main__":
    chatbot()
