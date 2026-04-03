import re

rules = [
    (r"hello", ["Hi there!", "Hello! How are you today?"]),
    (r"my name is (.*)", ["Nice to meet you %1!", "Hello %1, how are you feeling today?"]),
    (r"i feel (.*)", ["Why do you feel %1?", "Do you often feel %1?"]),
    (r"i am (.*)", ["How long have you been %1?", "Why are you %1?"]),
    (r"because (.*)", ["Is that the real reason?", "What other reasons might there be?"]),
    (r"(.*) mother (.*)", ["Tell me more about your mother.", "How is your relationship with your mother?"]),
    (r"i need (.*)", ["Why do you need %1?", "Would it really help you to get %1?"]),
    (r"my father (.*)", ["Tell me more about your father.", "How do you feel about your father?"]),
    (r"sad", ["Why do you feel sad?", "Do you often feel sad?"]),
    (r"happy", ["What makes you happy?", "Why do you feel happy?"]),
]

def respond(user_input):
    user_input = user_input.lower()
    for pattern, responses in rules:
        match = re.match(pattern, user_input)
        if match:
            response = responses[0]
            for i in range(1, len(match.groups()) + 1):
                response = response.replace(f"%{i}", match.group(i))
            return response
    return "Please tell me more."

def chat():
    print("Custom ELIZA Chatbot")
    print("Type 'quit' to stop.\n")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Good-bye.")
            break
        print(respond(user_input))
def get_eliza_response(user_input: str) -> str:
    return respond(user_input)

if __name__ == "__main__":
    chat()