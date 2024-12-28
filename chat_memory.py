import json

class ChatMemory:
    def __init__(self, config):
        self.config = config
        self.memory_path = config.get("memory_path", "chat_memory.json")
        self.chat_history = []

    def store_message(self, message):
        # Store the message in the chat history
        self.chat_history.append(message)
        self.save_memory()

    def load_memory(self):
        try:
            with open(self.memory_path, 'r') as file:
                self.chat_history = json.load(file)
        except FileNotFoundError:
            self.chat_history = []

    def save_memory(self):
        with open(self.memory_path, 'w') as file:
            json.dump(self.chat_history, file, indent=4)

    def display_memory(self):
        print("Chat History:")
        for message in self.chat_history:
            print(message)
