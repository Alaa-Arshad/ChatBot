# Define a function to handle user input and provide responses
def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase for easy matching
        
        # Responding to greetings
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        
        # Responding to "how are you?"
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        # Providing information about the bot
        elif "who are you" in user_input or "what are you" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot created to assist you with basic queries.")
        
        # Handling "thank you" or "thanks"
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! Happy to help.")
        
        # Handling "goodbye"
        elif "goodbye" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the chat loop
        
        # If the input doesn't match any of the predefined rules
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
            
# Run the chatbot
chatbot()
