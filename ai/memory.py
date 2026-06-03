class ConversationMemory:
    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_user(self, text):
        self.messages.append({'role': 'user', 'content': text})
        self.trim()

    def add_assistant(self, text):
        self.messages.append({'role': 'assistant', 'content': text})
        self.trim()

    def trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self):
        return self.messages
