import os
from dotenv import load_dotenv
from openai import OpenAI
from app.shared.sheets_data import get_sheets_data

def gpt_request(
    renovation_size="0",
    summary="",
    ) -> str:
    load_dotenv()
    key = os.getenv("OPEN_AI_KEY")

    client = OpenAI(api_key=key)
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Você é um especialista em reformas"},
                  {"role": "user", "content": f"Aqui estão os dados sobre preços para materiais e serviços {get_sheets_data()} em csv "+
                   f"o que estiver faltando, busque uma média de preços na internet, aqui estão os dados da reforma:"+
                   f"- tamanho da reforma: {renovation_size}\n"+
                   f"- resumo da reforma: {summary}\n"+
                   f"(o que estiver faltando ou zerado, é porque a reforma não necessitará desses materiais/serviços, portanto desconsidere)\n"+
                   f"Me responda apenas com esse formato: R$XX.XXX,XX - R$ XX.XXX,XX ou seja, um intervalo de um orçamento final para o cliente"}],
        temperature=0.2,
        max_tokens=256,
    )
    return res.choices[0].message.content