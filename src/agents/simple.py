from typing import TypedDict
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import AIMessage 


class State(MessagesState): 
    customer_name: str
    my_age: int

def node_1(state: State) -> None:
    if state.get("customer_name") is None:
        return {
            "customer_name": "Juan Perez",
        }
    else:
        ai_msg = AIMessage(content="Hello, how can I help you? Message from AI")
        return {
            "messages": [ai_msg],
        }

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()