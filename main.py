from src.graph import get_graph


if __name__ == "__main__":
  # Obtém o grafo
  graph = get_graph()

  # Define as mensagens de entrada do usuário
  inputs = {
    "messages": [
      {
        "role": "user",
        "content": "Summarize my latest 3 emails.",
      }
    ],
  }
  
  # Configuração com IDs de encadeamento e usuário para fins de autorização
  config = {"configurable": {"thread_id": "123456", "user_id": "gabrielsilveira.web@gmail.com"}}
  
  # Executa o grafo e transmite as saídas.
  for chunk in graph.stream(inputs, config=config, stream_mode="values"):
    # Pretty-print da última mensagem no chunk
    chunk["messages"][-1].pretty_print()