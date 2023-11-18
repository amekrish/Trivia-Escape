import openai
#openai.api_key = "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" 
from openai import OpenAI
#from config.env import OPENAI_API_KEY
#client = OpenAI(api_key="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")

import os
openai.api_key = os.environ['OPENAI_API_KEY']

# os.environ[“OPENAI_API_KEY”] = “your key here”
# prompt = "Generate an easy history question with 4 multiple choice options and a correct answer"
# model = "text-davinci-003"
# response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

# generated_text = response.choices[0].text
# print(generated_text)


# from openai import OpenAI
# client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
