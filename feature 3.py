from openai import OpenAI

client = OpenAI(api_key='my-api-key-here')

print("Hello! I'm a chatbot here to help you improve your time management skills.")
print("Please tell me what you're struggling with or what you'd like to improve and ask further questions:")
print("Enter 'exit' to stop talking to me. :)")
print()

inital = True

while True:

    user_query = input()

    if(user_query == 'exit'):
        break

    if inital:
        prompt = f"Given a student's question about time management: '{user_query}', provide detailed advice on improving time management skills."
    else:
        prompt = user_query
    inital = False

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Updated to use the Curie model
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print(response.choices[0].text.strip())
    print("Ask me further questions! or type 'exit'")
    print("")