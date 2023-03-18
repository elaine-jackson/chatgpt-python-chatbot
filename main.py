import openai

# Define variables.
def ask_chatgpt(messages):
    with open('openai-api-key.txt', 'r') as file:
        openai.api_key = file.read().replace('\n', '').replace(' ', '')

    # Configure the model and response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Return the first response from the API
    return response['choices'][0]['message']['content']

# Main program
print("Hi there. I'm ChatGPT using the gpt-3.5-turbo model! How can I assist you?\n")

# Array to store the chat contents
messages = []

while(True):
    prompt = input()

    if prompt == "quit":
        exit()

    messages.append({"role": "user", "content": prompt})

    answer = ask_chatgpt(messages)

    messages.append({"role": "assistant", "content": answer})

    print(answer + "\n")
