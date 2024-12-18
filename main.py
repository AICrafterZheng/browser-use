from langchain_openai import AzureChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

async def main():
    llm = AzureChatOpenAI(
        model="gpt-4o",
        api_version= os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_API_BASE", ""),
        api_key=os.getenv("AZURE_OPENAI_API_KEY_GPT_4o", ""),
    )
    task = "Please go to https://aicrafter.info/ to search 'cuda' in the 'Search articles' box"
    task = 'Please go to https://www.wsj.com/articles/amazon-announces-supercomputer-new-server-powered-by-homegrown-ai-chips-18c196fc, and extract the text. If you see captcha please solve it'
    task = "Please go to https://aicrafter.info/news/1810, and take a screenshot of the page, then save the screenshot to a file"
    task = "Please go to https://aicrafter.info/"
    task += ", and check if the subscribe button is clickable"
    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())