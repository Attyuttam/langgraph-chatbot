from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

tool = TavilySearch(max_results=2)
tools = [tool]
