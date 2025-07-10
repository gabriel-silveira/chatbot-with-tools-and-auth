from langchain_arcade import ToolManager
from langgraph.graph import MessagesState
from src.config import ARCADE_API_KEY

# Initialize tool manager
tools_manager = ToolManager(
  api_key=ARCADE_API_KEY,
)

# Initialize tools
langchain_tools = tools_manager.init_tools(
  toolkits=[
    #"Web",
    #"Search",
    "Google",
    #"Microsoft",
    #"Github",
    #"Slack",
    #"Linkedin",
    #"X",
    #"Confluence",
    #"Jira",
    #"Trello",
    #"Notion",
    #"Dropbox",
    #"Reddit",
  ],
)


# Função para lidar com a autorização para ferramentas que exigem isso
def authorize(state: MessagesState, config: dict):
    # Pega o ID do usuário
    user_id = config["configurable"].get("user_id")

    for tool_call in state["messages"][-1].tool_calls:
        # Pega o nome da ferramenta
        tool_name = tool_call["name"]

        # Verifica se a ferramenta precisa de autorização
        if not tools_manager.requires_auth(tool_name):
            continue

        auth_response = tools_manager.authorize(tool_name, user_id)

        if auth_response.status != "completed":
            # Solicite ao usuário que visite a URL para autorização
            print(f"Visit the following URL to authorize: {auth_response.url}")

            # Aguarde o usuário concluir a autorização
            # e depois verifique o status da autorização novamente
            tools_manager.wait_for_auth(auth_response.id)

            if not tools_manager.is_authorized(auth_response.id):
                # Interrompe a execução se a autorização falhar
                raise ValueError("Authorization failed")

    return {"messages": []}