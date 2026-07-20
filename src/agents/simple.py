from typing import TypedDict
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import AIMessage 
from langchain.chat_models import init_chat_model
import random, os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="gpt-4o-mini",
    temperature=1,
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    streaming=False,
)

class State(MessagesState): 
    customer_name: str
    my_age: int

def node_1(state: State) -> None:
    new_state: State = {}

    if state.get("customer_name") is None:
        new_state["customer_name"] = random.choice(["Alfred", "Fernando", "Juan", "David"])
    else:
        new_state["my_age"] = random.randint(18, 99)

    history = state.get("messages", [])
    ai_message = llm.invoke(history)
    new_state["messages"] = [ai_message]
    print(new_state)
    return new_state

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()