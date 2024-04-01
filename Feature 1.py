import openai
import time
import random

openai.api_key = "YOUR_API_KEY"

def generate_reminder():
    reminder_prompts = [
        "Write a friendly reminder encouraging the user to take a break from social media.",
        "Write a funny and lighthearted reminder to step away from the screen.",
        "Write a motivating reminder suggesting an alternative activity for a short break.", 
        "Write a reminder that emphasizes the importance of mindful social media use."
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": random.choice(reminder_prompts)}]
    )
    message = response.choices[0].message.content
    return message  

def timekeeper_chat():
    user_limit = int(input("How many minutes do you want to spend on social media? "))
    goal = input("What's your main goal for this social media session? (e.g., catch up, find an event, etc.) ")
    max_skips = 2  

    print("Great! Let's get started. I'll let you know when your time is up.") 
    print(f"Type 'skip' or 'end' anytime to finish early (max {max_skips} skips).")
    start_time = time.time()
    skips_used = 0

    while True:
        if time.time() - start_time > user_limit * 60:
            reminder = generate_reminder()
            print(f"{reminder} Remember, your goal was: {goal}")
            break  

        user_input = input()
        if user_input.lower() in ["skip", "end"]:
            if skips_used < max_skips:
                print("Okay, how about this instead:")
                reminder = generate_reminder() 
                print(reminder) 
                skips_used += 1
            else:
                print("You've reached the maximum number of skips. Time to focus!")
            continue  

if __name__ == "__main__":
    timekeeper_chat()
