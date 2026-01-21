from ollama import embed, chat

embeddings = embed(model="custom_qwen", input=["Here is an example sentence I will be embedding!", "Here's a second one!"])

print(len(embeddings['embeddings'][0]))

response = chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': 'Did Germany win the fifa 2022 world cup?',
  },
])

print(response.message.content)