
import os
import sys

from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller
import asyncio, time
from dotenv import load_dotenv
from pydantic import SecretStr
load_dotenv()

timestamp = int(time.time())

prompt = f"""
Acesse  este site "https://front.serverest.dev/login" Clique em "cadastre-se" faça um cadastro com o nome LucasTeste e com o email lucasgabrielsm7@gmail.com
E escolha a senha "12345678". Depois clique em "Cadastrar". E aguarde a pagina inicial carregar, quando isso acontecer o teste é finalizado com sucesso.



"""


async def main():
    agent = Agent(
        task=prompt,
        llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
        
    )
    
    result = await agent.run()
    
    print(result)
		
asyncio.run(main())