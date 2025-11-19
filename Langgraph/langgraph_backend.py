from langgraph.graph import StateGraph
from langgraph.constants import END
from typing import TypedDict

class MyState(TypedDict):
    message: str

def start_node(state: MyState) -> MyState:
    print("Start node received:", state["message"])
    return {"message": state["message"] + " -> processed by start"}

def end_node(state: MyState) -> MyState:
    print("End node received:", state["message"])
    return state

builder = StateGraph(MyState)

builder.add_node("start", start_node)
builder.add_node("end", end_node)

builder.set_entry_point("start")
builder.add_edge("start", "end")
builder.add_edge("end", END)

graph = builder.compile()

from langgraph.graph import StateGraph, END

# 1. Define your state
class MyState(TypedDict):
    message: str

# 2. Create graph
graph_builder = StateGraph(MyState)

# 3. Add nodes
def start_node(state):
    print("Start node running…")
    return {"message": "Hello"}

graph_builder.add_node("start", start_node)

# 4. Set entry point
graph_builder.set_entry_point("start")

# 5. Compile graph
graph = graph_builder.compile()

# 6. >>> PASTE THIS PART <<<
# Show the graph diagram
graph.display()    # Works in VS Code / Jupyter / Colab
# or
graph.visualize()
