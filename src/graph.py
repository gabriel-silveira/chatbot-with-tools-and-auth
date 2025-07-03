from langgraph.checkpoint.memory import MemorySaver
from src.workflow import get_workflow


def get_graph():
  # Obtém o workflow
  workflow = get_workflow()

  # Cria uma instância do nosso "salvador de memória"
  memory = MemorySaver()

  # Compila o workflow em um grafo executável.
  # O checkpointer garante que o estado seja salvo a cada passo.
  graph = workflow.compile(checkpointer=memory)

  return graph