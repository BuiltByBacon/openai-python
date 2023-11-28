import OpenAI
import os

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="What is the capital of France?",
    max_tokens=50
)

from openai import OpenAI

client = OpenAI()

completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))