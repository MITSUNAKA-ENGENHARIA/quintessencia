import os
from dotenv import load_dotenv
from openai import OpenAI

def gpt_request() -> str:
    load_dotenv()
    key = os.getenv("OPEN_AI_KEY")

    client = OpenAI(api_key=key)
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Você é um consultor de reformas, "+
                   "me diga as principais coisas que eu tenho que saber pra reformar meu apartamento"}],
        temperature=0.2,
        max_tokens=256,
    )
    return res.choices[0].message.content