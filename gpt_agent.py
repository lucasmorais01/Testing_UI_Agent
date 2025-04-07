
import os
import sys

from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
import asyncio, time
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

timestamp = int(time.time())

prompt = f"""
Pesquise sobre a empresa "Tesla".
Depois carregue a pagina e volte para a tela inicial de pesquisa do google e pesquise "palmeiras".
"""


async def main():
    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(model="gpt-4o", api_key=SecretStr(os.getenv('OPENAI_API_KEY')))
        
    )
    result = await agent.run()
    
    print(result)
		
asyncio.run(main())