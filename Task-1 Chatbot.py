#Predefining some responses
negative_respones=("no","nah","nope","bad","worse","not great","no thanks","sorry")
positive_responses=("yes","yep","yeah","ok","good","great","thanks","awesome")
greetings=("hi","hello","hey","yo")
exiting=("bye","goodbye","ta ta")

#defining a function for the chatbot to respond the user's input
def chatbot_response(user_input):
    user_input = user_input.lower()
 #predfining the contents which the chatbot can respond to   
    if user_input in greetings:
        return "Hi there! How are you?"
    elif user_input == "good,how about you?":
        return "Nice,I am just a program but thanks for asking!.Then how was your day?"
    elif user_input in positive_responses:
        return "Its good to hear"
    elif user_input in negative_respones:
        return "Sorry to hear about it"
    elif user_input in exiting:
        return "Goodbye! Have a great day!"
    elif user_input == "can you help me?":
        return "Sure, I can help you. What do you need assistance with?"
    elif user_input == "what can you do?":
        return "I can chat with you based on predefined rules. Try asking me something!"
    elif user_input == "who is india's prime minister?":
        return "It is Mr.Narendra Modi.Is there anything else you want to ask?"
    else:
        return "I'm sorry, I don't understand that.Can you try it again?"
    
#defining a funtion to start the chatbot
    
def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

start_chatbot()
    

     



   



