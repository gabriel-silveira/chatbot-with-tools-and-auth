"""
Este é um agente que pode usar ferramentas para resolver problemas.
Neste exemplo, vamos utilizar a ferramenta de email do Google, o Gmail.

Exemplo de mensagem: "Faça um resumo dos meus últimos 3 e-mails não lidos"

Para autorizar a ferramenta, você precisará visitar a URL que será exibida no console.
Depois de autorizar, a ferramenta poderá ser usada normalmente.

Para encerrar o chat, digite 'sair'.
"""
from src.graph import get_graph


if __name__ == "__main__":
  graph = get_graph()

  # Loop para aguardar input do usuário
  while True:
    try:
      print("\nDigite sua mensagem (ou 'sair' para encerrar): ")
      user_input = input("> ")
      
      if user_input.lower() == 'sair':
        print("Encerrando o chat...")
        break
      
      # Define as mensagens com o input do usuário
      inputs = {
        "messages": [
          {
            "role": "user",
            "content": user_input,
          }
        ],
      }
      
      # Configuração com IDs de encadeamento e usuário para fins de autorização
      config = {"configurable": {"thread_id": "123456", "user_id": "gabrielsilveira.web@gmail.com"}}
      
      # Executa o grafo e transmite as saídas.
      for chunk in graph.stream(inputs, config=config, stream_mode="values"):
        # Pretty-print da última mensagem no chunk
        chunk["messages"][-1].pretty_print()
        
    except KeyboardInterrupt:
      print("\nPrograma interrompido pelo usuário.")
      break
    except Exception as e:
      print(f"\nErro: {e}")