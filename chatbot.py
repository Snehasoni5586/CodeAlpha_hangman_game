# CodeAlpha Internship - Task 4
# Basic Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hey! Welcome to my chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hey":
            print("Chatbot: Hey! How are you?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Call the function
chatbot()