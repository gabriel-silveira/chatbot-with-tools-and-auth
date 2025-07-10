from langgraph.graph import END, MessagesState
from src.llm import llm_with_tools
from src.tools import tools_manager


# Função para invocar o modelo de linguagem e obter uma resposta
def call_agent(state: MessagesState):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)

    # Retorna o histórico atualizado de mensagens
    return {"messages": [response]}


# Essa função irá inspecionar a resposta do agente e retornar uma string: "authorization", "tools", ou "END".
def should_continue(state: MessagesState):
    # Pega a última mensagem e verifica se o agente decidiu usar uma ferramenta
    if state["messages"][-1].tool_calls:
        for tool_call in state["messages"][-1].tool_calls:
            # verifica se a ferramenta precisa de autorização
            if tools_manager.requires_auth(tool_call["name"]):
                return "authorization"
        return "tools"  # Prossiga para a execução da ferramenta se nenhuma autorização for necessária
    return END  # Termine o fluxo de trabalho se nenhuma ferramenta estiver presente
