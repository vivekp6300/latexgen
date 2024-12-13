import os
from openai import OpenAI
from dotenv import load_dotenv

OPENAI_KEY_NAME="OPEN_AI_KEY"
NO_OPENAI_KEY_ERR="No OPEN AI Key Found. Exiting()"
GPT_MODEL="gpt-4"

def ask_chatgpt(prompt):
    load_dotenv()
    api_key=os.getenv(OPENAI_KEY_NAME) or exit(NO_OPENAI_KEY_ERR)
    client=OpenAI(api_key=api_key)
    response=client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content

print(ask_chatgpt("What is the temperature in Delhi today?"))