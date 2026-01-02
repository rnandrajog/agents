from email import message
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

openai = OpenAI()

content ="pick a business area that might be worth exploring for an Agentic AI opportunity"
messages = [{"role": "user", "content":content}]

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

business_area = response.choices[0].message.content
print("Suggested business area for Agentic AI opportunity:", business_area)

content="Present a pain-point in the industry " + business_area

messages = [{"role": "user", "content": content}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
pain_point = response.choices[0].message.content
print(f"Pain-point in the industry ({business_area}):", pain_point)

content="propose the agentic AI solution for the pain-point area identified"
messages = [{"role": "user", "content": content + pain_point}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
solution = response.choices[0].message.content
print(" --------------------------------------------- the solution is -----------------------------------------")
print(f"Agentic AI solution for the pain-point in {business_area}:", solution)


