from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent

from agent.my_llm import llm
from agent.tools.tool_demo6 import runnable_tool
from agent.tools.tool_demo7 import MySearchTool

# 创建一个网络搜索的工具
search_tool = MySearchTool()

checkpointer = InMemorySaver()

agent = create_react_agent(
    llm,
    # tools=[calculate4, runnable_tool, search_tool, get_user_info_by_name],
    tools=[ runnable_tool, search_tool],
    prompt='您是一个智能助手，尽可能地调用工具回答用户的问题',
    checkpointer=checkpointer,
)