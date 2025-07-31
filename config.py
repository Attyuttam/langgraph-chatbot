import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.tavily_search_tool import tools

load_dotenv()

config = {"configurable": {"thread_id": "1"}}
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0).bind_tools(tools)

SYSTEM_MESSAGE = "You are a helpful assistant."
