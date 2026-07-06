import os
from openai import OpenAI

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)
response = client.chat.completions.create(
    model="qwen3.5:9b",
    messages=[
        {"role": "system", "content": "很高兴见到你!"},
        {"role": "user", "content": "假如教员在现在复活,会发生什么?"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)