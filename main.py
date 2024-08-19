from nlp import process_input_with_pattern

def Tiny_Chxikvi():
    print("Tiny_Chxikvi: Hello! I'm Tiny_Chxikvi. How can I help you today?")
    while True:
        user_input = input("You: ")
        
        response = process_input_with_pattern(user_input)
        print(f"Tiny_Chxikvi: {response}")
        
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    Tiny_Chxikvi()