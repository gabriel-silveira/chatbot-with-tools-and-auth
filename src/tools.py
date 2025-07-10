from langchain_arcade import ToolManager
from langgraph.prebuilt import ToolNode
from src.config import ARCADE_API_KEY

# Initialize the tool manager and fetch tools compatible with langgraph
tool_manager = ToolManager(api_key=ARCADE_API_KEY)
tools = tool_manager.init_tools(toolkits=["Google"])
tool_node = ToolNode(tools)