from openai import OpenAI
from typing import List, Dict
from pprint import pprint

client = OpenAI()

def get_response(messages: List[Dict[str, str]]) -> str:
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-0125', 
        messages=messages,
        temperature=0,
        seed=0       
    )
    assistant_response = response.choices[0].message.content
    messages.append(
        {
            'role': 'assistant', 
            'content': assistant_response
        }
    )
    
    return assistant_response

messages = [
    {
        'role': 'system', 
        'content': 'You are a helpful assistant'
    }
]

while True:
    query = input('(Type Query)> ')
    if query.strip().lower() == 'bye':
        break
    messages.append(
        {
            'role': 'user', 
            'content': query
        }
    )
    response = get_response(messages)
    print(f'# {response}')
    