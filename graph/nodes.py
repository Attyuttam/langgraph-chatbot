from config import llm
from graph.state import State

def chatbot(state: State) -> State:
    return {"messages": [llm.invoke(state["messages"])]}
