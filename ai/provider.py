import os
from openai import OpenAI


def get_client(provider='deepseek'):
    if provider == 'deepseek':
        return OpenAI(
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            base_url='https://api.deepseek.com'
        )

    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def chat(prompt, provider='deepseek'):
    client = get_client(provider)

    model = 'deepseek-chat' if provider == 'deepseek' else 'gpt-4o-mini'

    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'You are Jarvis, a helpful AI assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )

    return response.choices[0].message.content
