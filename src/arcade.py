from langchain_arcade import ArcadeToolManager
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from src.config import ARCADE_API_KEY

# Initialize the tool manager and fetch tools compatible with langgraph
tool_manager = ArcadeToolManager(api_key=ARCADE_API_KEY)
tools = tool_manager.get_tools(toolkits=["Google"])
tool_node = ToolNode(tools)

# Create a language model instance and bind it with the tools
model = ChatOpenAI(model="gpt-4o")
model_with_tools = model.bind_tools(tools)