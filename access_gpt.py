# Import the os package
import os

# Import the openai package
import openai

# Set openai.api_key to the OPENAI environment variable
openai.api_key = os.environ["OPENAI"]

CONTINUE = True

def chat(system, user_assistant):
    assert isinstance(system, str), "`system` should be a string"
    assert isinstance(user_assistant, list), "`user_assistant` should be a list"
    system_msg = [{"role": "system", "content": system}]
    user_assistant_msgs = [
        {"role": "assistant", "content": user_assistant[i]} if i % 2 else {"role": "user", "content": user_assistant[i]}
        for i in range(len(user_assistant))]

    msgs = system_msg + user_assistant_msgs
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=msgs)
    status_code = response["choices"][0]["finish_reason"]
    assert status_code == "stop", f"The status code was {status_code}."
    return response["choices"][0]["message"]["content"]

print("Welcome to IntelliVerify, enter 'EXIT' to exit.")
while CONTINUE:
    question = input("\nPlease enter your question: ")
    if question == 'EXIT': CONTINUE = False
    else:
        response = chat("You are very knowledgeable.", [question])
        print("ChatGPT: ", response,"\n")