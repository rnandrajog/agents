from dotenv import load_dotenv
import os
from openai import OpenAI


# load the environment variables from the .env file
load_dotenv(override=True)

# get the OpenAI API key from the environment variables
openai_api_key= os.getenv("OPENAI_API_KEY")

if openai_api_key is None or openai_api_key == "":
   #  print("OPENAI_API_KEY is not set")
     raise ValueError("OPENAI_API_KEY is not set")
   
else:
    print("key loaded")

# create a new OpenAI client
openai = OpenAI()
#messages =[{"role":"user", "content":"what is 4+3"}]
question ="Please propose a hard, challenging question to assess someone's IQ, Respond only with question."
messages =[{"role":"user", "content":question}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
#store the question in the question variable
question =response.choices[0].message.content
print(question)

messages =[{"role":"user", "content":question}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
answer = response.choices[0].message.content
print(answer)

