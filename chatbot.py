# Chatbot
import random
def get_response(user_input):
    user_input = user_input.lower()
    
    greetings = ['hello', 'hi', 'hey', 'greetings','vanakkam']
    greeting_responses = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!','vanakkam!']
    

    for word in user_input.split():
        if word in greetings:
            return random.choice(greeting_responses)
    
    return "I'm sorry, I don't understand. Can you please rephrase?"

while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("ChatBot:", response)
