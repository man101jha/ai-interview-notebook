# ── Coding Q2: Simple AI Agent with Tool Use ──────────────────────────────


# pip install langchain langgraph langchain-groq
# export GROQ_API_KEY="your_key_here"




import os
from typing import Annotated
from typing_extensions import TypedDict

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

# ---------------------------------------------------------
# 1. DEFINE TOOLS
# ---------------------------------------------------------
@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # Mocked — replace with a real weather API call
    fake_data = {
        "mumbai": "32°C, humid, light rain",
        "delhi": "38°C, clear sky",
        "bangalore": "26°C, cloudy"
    }
    return fake_data.get(city.lower(), f"No weather data found for {city}")

@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression, e.g. '23 * 7 + 1'."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

tools = [get_weather, calculator]

# ---------------------------------------------------------
# 2. DEFINE STATE
# ---------------------------------------------------------
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# ---------------------------------------------------------
# 3. INIT LLM (Groq via init_chat_model) + BIND TOOLS
# ---------------------------------------------------------
llm = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0
)
llm_with_tools = llm.bind_tools(tools)

# ---------------------------------------------------------
# 4. DEFINE NODES
# ---------------------------------------------------------
def agent_node(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

tool_node = ToolNode(tools)

# ---------------------------------------------------------
# 5. BUILD GRAPH
# ---------------------------------------------------------
graph_builder = StateGraph(AgentState)

graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "agent")
graph_builder.add_conditional_edges(
    "agent",
    tools_condition,   # routes to "tools" if LLM called a tool, else END
)
graph_builder.add_edge("tools", "agent")  # loop back after tool execution

graph = graph_builder.compile()

# ---------------------------------------------------------
# 6. RUN
# ---------------------------------------------------------
def main():
    user_input = "What's the weather in Mumbai, and what's 45 * 12?"

    result = graph.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })

    for msg in result["messages"]:
        msg.pretty_print()

if __name__ == "__main__":
    main()