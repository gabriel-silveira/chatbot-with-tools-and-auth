from langchain_arcade import ArcadeToolManager
from langgraph.prebuilt import ToolNode
from src.config import ARCADE_API_KEY

# Initialize the tool manager and fetch tools compatible with langgraph
tool_manager = ArcadeToolManager(api_key=ARCADE_API_KEY)
tools = tool_manager.get_tools(toolkits=["Google"])
tool_node = ToolNode(tools)