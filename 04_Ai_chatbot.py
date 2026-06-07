# Project : To create a AI chatbot assistant using pythons core logic - sring matching, functions, dictionaries, and loops

import datetime
import time

presenthour = datetime.datetime.now().hour
time.sleep(2)

user = input("Please Enter your name: ")
if 5<=presenthour<=12:
    print("Good morning,", user)
elif 13<=presenthour<=16:
    print("Good afternoon,", user)
elif 17<=presenthour<=20:
    print("Good Evening,", user)
else:
    print("Good night,", user)

print("Welcome!! to your AI ChatBot")
print(f"Hello {user}, you can ask me a some basic questions?? or click 'bye' to exit from the Bot")

usermood = input("Are you feeling sad or happy today?: ").lower()
if "happy" in usermood:
    print("That's great. Lets keep vibing.")
elif "sad" in usermood:
    print("I am sorry to hear that. Here's a vibing hug from me to keep you cheers.")
else:
    print("sorry, i didn't quite catch that.")

# memory creation of ai chatbot using dictionaries

responses = { "hello": "Hii!, Welcome how can I help you??",
              "how are you": "I am fine!!",
              "who are you": "I am your chatbot assistant , here to solve your questions or doubts.",
              "ohh happy": "Yess i am also , great to hear you!!",
              "give me some motivation": "just focus on your career , and solving the bug in the coding makes you the intelligence developer",
              "what is function": "Jaakar chapter 7 padho",
              "how can you help me": "I can easily help you by making the concept more clear and easy to understand",
              "define Python": "It is a programming language where we interact with computers to perform various task",
              "Why AI is imp": "AI are rapidly growing in every field to make the work more easier and prevents time",
              "bye": "Okk bye!!, nice to meet you"  }

# using function to get response of chatbot
def getResponseofbot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to tell that , still i am trying to learn it as soon as possible."

# take user input

while True:
    userinput = input("Please ask your question??: ")
    reply = getResponseofbot(userinput)
    time.sleep(1)    
    print("Respone: ",reply)

    if "bye" in userinput.lower():
        break