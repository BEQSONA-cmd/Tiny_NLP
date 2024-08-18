from nlp import process_input

def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        
        response = process_input(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    chatbot()