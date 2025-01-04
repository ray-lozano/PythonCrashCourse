messages = ['hello', 'goodbye', 'how are you']
sent_messages = []

def show_message(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"\nSent message: {current_message}")
        sent_messages.append(current_message)

show_message(messages)
send_messages(messages[:], sent_messages)
show_message(messages)
show_message(sent_messages)