import openai
import time
import random

openai.api_key = "YOUR_API_KEY"

def ask_question():
    questions = [
        "How does social media make you feel right now compared to before you started scrolling?",
        "What's one positive thing you could do instead of scrolling?",
        "Could you try closing your eyes for a minute and focusing on your breath instead?",
        "What's something productive you could accomplish with the time you'd spend scrolling?",
        "Are you getting closer to your goals by scrolling, or further away?",
        "What emotions or thoughts do you experience when you're on social media for extended periods?",
        "Are there specific triggers or situations that lead you to use social media excessively?",
        "How has your social media use affected your daily life, relationships, and academic performance?",
        "What goals or aspirations do you have that might be hindered by your social media addiction?", 
        "What are your reasons for wanting to reduce or eliminate your social media use?",
        "What obstacles do you anticipate encountering as you try to cut back on social media?",
        "How have previous attempts to limit social media use been challenging or unsuccessful?",
        "What alternative activities or hobbies could you engage in when you feel the urge to use social media excessively?",
        "How do you define a healthy balance between social media usage and other aspects of your life?"
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or another suitable GPT-3 model
        messages=[{"role": "user", "content": random.choice(questions)}]
    )

    message = response.choices[0].message.content
    print(message) 

while True:
    user_input = input("Do you want a mindful question? (yes/no): ")
    if user_input.lower() == "yes":
        ask_question()
    else:
        break
