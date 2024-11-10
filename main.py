import os
#import PyPDF2
import prompts
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

model = "gpt-4-turbo-preview"
temperature = 0.3
max_tokens = 500
topic = ""

#read the pdf file
book = ""
#file_path = "naval"


#promopts
system_message = prompts.system_message
prompt = prompts.generate_prompt(book,"")

messages=[
    {"role": "system", "content": "You are useful"},
    {"role": "user", "content": "hi"}
]


#helper function

def get_summary():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content

print(get_summary())

# const openai = new OpenAI();

# const completion = await openai.chat.completions.create({
#     model: "gpt-4o-mini",
#     messages: [
#         { role: "system", content: "You are a helpful assistant." },
#         {
#             role: "user",
#             content: "Write a haiku about recursion in programming.",
#         },
#     ],
# });