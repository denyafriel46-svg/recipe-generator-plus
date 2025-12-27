from uttils import llama, llama_chat

# Prompt pertama
response1 = llama("What are fun activities I can do this weekend?")
print("AI:", response1.message.content)

# Ambil string dari ChatResponse
response_text1 = response1.message.content

# Multi-turn chat
prompts = [
    "What are fun activities I can do this weekend?",
    "Which of these would be good for my health?"
]
responses = [response_text1]  # simpan jawaban sebagai string

response2 = llama_chat(prompts, responses)
print("AI:", response2.message.content)
