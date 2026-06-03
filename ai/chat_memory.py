from ai.provider import get_client

class ChatMemory:
    def __init__(self, provider='deepseek', max_history=20):
        self.provider = provider
        self.max_history = max_history
        self.messages = [
            {'role': 'system', 'content': 'You are Jarvis, a helpful AI assistant.'}
        ]

    def ask(self, prompt):
        self.messages.append({'role': 'user', 'content': prompt})

        if len(self.messages) > self.max_history:
            self.messages = [self.messages[0]] + self.messages[-(self.max_history-1):]

        client = get_client(self.provider)
        model = 'deepseek-chat' if self.provider == 'deepseek' else 'gpt-4o-mini'

        response = client.chat.completions.create(
            model=model,
            messages=self.messages
        )

        answer = response.choices[0].message.content
        self.messages.append({'role': 'assistant', 'content': answer})

        return answer
