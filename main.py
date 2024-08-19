import logging
import time
from nlp import process_input_with_pattern

logging.basicConfig(filename='Tiny_Cxikvi.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def print_chars(name, message):
    print(f"{name} ", end='')
    delay = 0.03
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def Tiny_Cxikvi():
    logging.info("Tiny_Cxikvi started.")
    print_chars("Tiny_Cxikvi:", "Hello! How can I help you today?")
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print_chars("Tiny_Cxikvi:", "Goodbye! Have a great day.")
            logging.info("User ended the conversation with 'bye'.")
            break
        
        logging.info(f"User input: {user_input}")
        
        response = process_input_with_pattern(user_input)
        print_chars(f"Tiny_Cxikvi:", response)
        
        logging.info(f"Tiny_Cxikvi response: {response}")

if __name__ == "__main__":
    Tiny_Cxikvi()
