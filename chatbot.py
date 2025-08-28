import random
import datetime

# Knowledge base (patterns → answers)
qa_pairs = {
    "hello": ["Hi there!", "Hello 👋", "Hey! How are you?"],
    "hi": ["Hello!", "Hi! Nice to see you."],
    "how are you": ["I'm doing great, thanks!", "All good here 😊", "Feeling awesome!"],
    "your name": ["I'm PyBot 🤖, your personal assistant.", "You can call me ChatBuddy."],
    "who created you": ["I was created by Abhay in Python.", "Abhay built me as a project!"],
    "what is python": [
        "Python is a high-level programming language, easy to learn and very powerful.",
        "Python is used for web development, AI, data science, and more."
    ],
    "what is bca": [
        "BCA stands for Bachelor of Computer Applications, a 3-year undergraduate course in computer science.",
        "BCA is a degree focused on programming, software, and computer fundamentals."
    ],
    "time": [lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "date": [lambda: f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}"],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs 🐞.",
        "Why was the computer cold? Because it left its Windows open!",
        "Why did the Java developer go broke? Because he used up all his cache 💸."
    ],
    "bye": ["Goodbye!", "See you later!", "Bye 👋, take care!"]
}

def chatbot():
    print("PyBot 🤖: Hi! I'm your chatbot. Ask me anything. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        found = False
        for key in qa_pairs:
            if key in user_input:  # keyword/pattern matching
                response = random.choice(qa_pairs[key])
                if callable(response):   # for dynamic answers (time/date)
                    response = response()
                print("PyBot 🤖:", response)
                found = True
                if key == "bye":
                    return
                break

        if not found:
            print("PyBot 🤖: Sorry, I don’t know that yet. Try asking about Python, BCA, time, or a joke.")

# Run chatbot
chatbot()
