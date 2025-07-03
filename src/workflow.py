
from src.agents import call_agent, should_continue, authorize
from src.tools import tool_node
from langgraph.graph import END, START, MessagesState, StateGraph


def get_workflow():
  """Obtém o workflow (nós e arestas)"""

  # Cria um novo grafo de fluxo de trabalho.
  # Ele sabe que vai gerenciar um estado do tipo MessagesState.
  workflow = StateGraph(MessagesState)

  # Adiciona o nó "agent": quando ativado, ele chama a função call_agent.
  workflow.add_node("agent", call_agent)
  # Adiciona o nó "tools": responsável por executar ferramentas.
  workflow.add_node("tools", tool_node)
  # Adiciona o nó "authorization": para lidar com a autorização.
  workflow.add_node("authorization", authorize)

  # Define a primeira aresta: do ponto inicial, vá para o nó "agent".
  workflow.add_edge(START, "agent")

  # Após o nó "agent", chame a função should_continue para decidir o próximo passo.
  workflow.add_conditional_edges(
    "agent",
    should_continue, # A função que toma a decisão
    ["authorization", "tools", END], # Os destinos possíveis
  )

  # Se o fluxo for para "authorization", o próximo passo deve ser "tools".
  workflow.add_edge("authorization", "tools")

  # Após executar as ferramentas, volte para o agente.
  workflow.add_edge("tools", "agent")

  return workflow