def get_bot_response(user_input):
    cleaned_input = user_input.lower().strip()
    
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif "how are you" in cleaned_input:
        return "I'm fine, thanks! (Even though I am just a simple Python script)."
    elif cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that. Try saying hello!"
def start_chat():
    print("   Chatbot Initialized   ")
    print("Type 'bye' or 'exit' to end the conversation.\n")
    while True:
 
        message = input("You: ")
        
        reply = get_bot_response(message)
        
        print(f"Bot: {reply}")
        if reply == "Goodbye!":
            break
start_chat()