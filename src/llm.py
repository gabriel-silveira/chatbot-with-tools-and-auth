from langchain_openai import ChatOpenAI
from src.tools import tools

# Create a language model instance and bind it with the tools
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)