from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph
from src.flow import call_agent, should_continue, authorize
from src.arcade import tool_node


if __name__ == "__main__":
    # Build the workflow graph using StateGraph
    workflow = StateGraph(MessagesState)
 
    # Add nodes (steps) to the graph
    workflow.add_node("agent", call_agent)
    workflow.add_node("tools", tool_node)
    workflow.add_node("authorization", authorize)
 
    # Define the edges and control flow between nodes
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, ["authorization", "tools", END])
    workflow.add_edge("authorization", "tools")
    workflow.add_edge("tools", "agent")
 
    # Set up memory for checkpointing the state
    memory = MemorySaver()
 
    # Compile the graph with the checkpointer
    graph = workflow.compile(checkpointer=memory)

    # Define the input messages from the user
    inputs = {
      "messages": [
        {
          "role": "user",
          "content": "Summarize my latest 3 emails.",
        }
      ],
    }
    
    # Configuration with thread and user IDs for authorization purposes
    config = {"configurable": {"thread_id": "123456", "user_id": "gabrielsilveira.web@gmail.com"}}
    
    # Run the graph and stream the outputs
    for chunk in graph.stream(inputs, config=config, stream_mode="values"):
      # Pretty-print the last message in the chunk
      chunk["messages"][-1].pretty_print()