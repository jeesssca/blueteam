import streamlit as st
import requests

# Set your OpenAI API key
api_key = "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"

def generate_reminder(addiction_level):
    try:
        prompt = f"Write a motivational and supportive reminder to help someone reduce their social media addiction. Take into account their addiction level: {addiction_level}"

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a friendly assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
        ).json()

        print("OpenAI Response (Reminder):", response)  # Debugging line

        if 'choices' in response:
            return response['choices'][0]['message']['content']
        else:
            return f"An error occurred while generating the reminder: {response}"
    except Exception as e:
        print("Error:", e)
        return f"An error occurred while generating the reminder: {e}"

def generate_goal_conversation(addiction_level, interests):
    try:
        prompt = f"Start a conversation to set goals and strategies for reducing social media usage. Take into account addiction level: {addiction_level} and interests: {interests}."

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a friendly assistant."},
                    {"role": "user", "content": prompt}
                ]
            }
        ).json()

        print("OpenAI Response (Goal Conversation):", response)  # Debugging line

        if 'choices' in response:
            return response['choices'][0]['message']['content']
        else:
            return f"An error occurred while generating the goal-setting conversation: {response}"
    except Exception as e:
        print("Error:", e)
        return f"An error occurred while generating the goal-setting conversation: {e}"

# Streamlit App
st.title("Social Media Limitation Assistant")

addiction_level = st.selectbox("How strong is your social media addiction?", 
                               ["Mild", "Moderate", "Strong"])

interests = st.text_input("What are your hobbies or interests?")

if st.button("Generate Reminder"):
    reminder = generate_reminder(addiction_level)
    st.write("Reminder:")
    st.write(reminder)

if st.button("Start Goal Setting Conversation"):
    goal_conversation = generate_goal_conversation(addiction_level, interests)
    st.write("Goal Setting Conversation:")
    st.write(goal_conversation)
