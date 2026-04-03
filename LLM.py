from transformers import pipeline
import threading

generator = None

def load_generator():
    global generator
    generator = pipeline("text-generation", model="gpt2")

# Start loading in a background thread
threading.Thread(target=load_generator, daemon=True).start()

def get_llm_response(user_input: str) -> str:
    global generator
    # If it's still loading, give a temporary message
    if generator is None:
        return "(LLM is still loading, please wait...)"
    result = generator(user_input, max_new_tokens=50, do_sample=True)
    return result[0]['generated_text']