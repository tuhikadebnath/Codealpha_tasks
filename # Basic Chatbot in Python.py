# Basic Chatbot in Python

def chatbot():
    print("================================")
    print("        BASIC CHATBOT")
    print("================================")
    print("Hello! I am a simple chatbot.")
    print("You can say: hello, how are you, or bye.")
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

        print()


if __name__ == "__main__":
    chatbot()