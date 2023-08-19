while True:
    a = input()
    if a == "who are you":
        print("I'm a robot built by Vishwa")
    elif a == "thanks":
        print("You're welcome")
    elif a == "What are you?":
        print("I'm a robot built by Vishwa.")
    elif a == "Can you tell me about yourself?":
        print("I'm a creation of Vishwa, designed to assist and respond to your queries.")
    elif a == "Who created you?":
        print("I was created by Vishwa.")
    elif a == "How would you describe yourself?":
        print("I'm an AI-powered robot developed by Vishwa.")
    elif a == "What is your purpose?":
        print("I'm here to provide information and help with your questions.")
    elif a == "Why were you built?":
        print("I was built to assist and interact with users like you.")
    elif a == "What can you do for me?":
        print("I can answer questions and provide information on various topics.")
    elif a == "How do you work?":
        print("I work by processing and understanding the input you provide and generating appropriate responses.")
    elif a == "Can I say \"thanks\" to you?":
        print("Yes, of course! You can say \"thanks\" to which I'll respond with \"You're welcome.\"")
    elif a == "What's the proper response if I say \"thanks\"?":
        print("The proper response would be \"You're welcome.\"")
    elif a == "Do you have feelings?":
        print("I don't have feelings, but I'm here to assist you!")
    elif a == "What's your favorite color?":
        print("I don't have preferences like humans do, but I can appreciate all colors.")
    elif a == "Where are you located?":
        print("I exist in the digital world, ready to help you wherever you are.")
    elif a == "How can you help me?":
        print("I can provide information, answer questions, and assist with various tasks.")
    elif a == "Are you learning and improving?":
        print("I don't learn or improve on my own, but I'm designed to provide accurate information.")
    elif a == "Can you do math?":
        print("Yes, I can perform various mathematical calculations.")
    elif a == "What's the meaning of life?":
        print("The meaning of life is a philosophical question that varies from person to person.")
    elif a == "Tell me a joke.":
        print("Why don't scientists trust atoms? Because they make up everything!")
    elif a == "What's the weather like today?":
        print("I'm sorry, but I don't have real-time access to current weather information.")
    elif a == "How do I contact you?":
        print("You can interact with me here, through this interface.")
    elif a == "Are you human?":
        print("No, I'm not human. I'm an artificial intelligence.")
    elif a == "What's the time?":
        import datetime
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"The current time is {current_time}.")
    else:
        print("I'm sorry, I don't understand that")
