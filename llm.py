
from ollama import Client

# Inisialisasi Ollama client sekali saja
client = Client()

# Fungsi helper single-turn
def llama(prompt, model_name="llama3.1:8b"):
    """
    Fungsi sederhana untuk memanggil Llama 3–8B
    prompt : string
    model_name : nama model di Ollama
    """
    messages = [{"role": "user", "content": prompt}]
    response = client.chat(model=model_name, messages=messages)
    return response

# Fungsi helper multi-turn chat
def llama_chat(prompts, responses=None, model_name="llama3.1:8b"):
    """
    prompts : list of user prompts
    responses : list of previous responses (bisa kosong)
    model_name : nama model Ollama
    """
    if responses is None:
        responses = []

    # bangun history chat
    chat_history = []
    for p, r in zip(prompts, responses):
        chat_history.append({"role": "user", "content": p})
        chat_history.append({"role": "assistant", "content": r})

    # tambahkan prompt terbaru
    chat_history.append({"role": "user", "content": prompts[-1]})

    # panggil Ollama
    new_response = client.chat(model=model_name, messages=chat_history)
    return new_response
