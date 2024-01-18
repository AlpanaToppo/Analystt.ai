import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
pairs = [
    ("hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]),
    ("how are you", ["I'm good, thank you.", "I'm doing well."]),
    ("what is your name", ["I am a chatbot.", "You can call me ChatGPT."]),
    ("bye|goodbye", ["Goodbye!", "See you later."]),
    (r"my name is (.*)", ["Nice to meet you, %1!"]),
    (r"what is your favorite (color|movie|food)", ["I don't have preferences."]),
    (r"(.*) (weather|temperature) in (.*)", ["I'm sorry, I cannot provide real-time weather information."]),
    (r"(.*)", ["I'm not sure how to respond to that."]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm a simple chatbot. You can start chatting with me or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    # Download NLTK data if not already present
    nltk.download('punkt')

    # Start the chat
    start_chat()
