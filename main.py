from langchain_core.messages import HumanMessage, AIMessage

from graph.builder import compile_graph
from config import config

# def stream_graph_updates(user_input: str):
#     for event in compile_graph().stream({"messages": [{"role": "user", "content": user_input}]}):
#         for value in event.values():
#             print("Assistant:", value["messages"][-1].content)

def stream_graph_updates(user_input: str):
    final_message = None
    for event in compile_graph().stream({"messages": [HumanMessage(content=user_input)]}):
        for value in event.values():
            messages = value["messages"]
            if messages:
                last_msg = messages[-1]
                # Use attribute access instead of dict indexing
                if isinstance(last_msg,AIMessage) and isinstance(last_msg.content, str):
                    final_message = last_msg.content
    if final_message:
        print("Assistant:", final_message)


if __name__ == '__main__':
    print("Hello LangGraph")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
