from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from graph.state import State
from graph.nodes import chatbot
from tools.tavily_search_tool import tools
from memory.memory_saver import memory

tool_node = ToolNode(tools)

def compile_graph():
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)

    # # The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "END" if
    # # it is fine directly responding. This conditional routing defines the main agent loop.
    # graph_builder.add_conditional_edges(
    #     "chatbot",
    #     route_tools,
    #     # The following dictionary lets you tell the graph to interpret the condition's outputs as a specific node
    #     # It defaults to the identity function, but if you
    #     # want to use a node named something else apart from "tools",
    #     # You can update the value of the dictionary to something else
    #     # e.g., "tools": "my_tools"
    #     {"tools": "tools", END: END},
    # )

    # The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "END" if
    # it is fine directly responding. This conditional routing defines the main agent loop.
    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition
    )
    graph_builder.add_node("tools", tool_node)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph_builder.add_edge("tools", "chatbot")

    return graph_builder.compile()

# Optional: for debugging flow
if __name__ == "__main__":
    compiled_graph = compile_graph()
    print(compiled_graph.get_graph().draw_mermaid())
