from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from agent.tools.tool_demo3 import calculate3
from agent.tools.tool_demo4 import calculate4
from agent.tools.tool_demo6 import runnable_tool
from agent.tools.tool_demo7 import MySearchTool

# 创建一个网络搜索的工具
search_tool = MySearchTool()

# 本地私有化部署的大模型
llm = ChatOpenAI(
    model='qwen3-8b',
    temperature=0.8,
    api_key='xx',
    base_url="http://localhost:6006/v1",
    extra_body={'chat_template_kwargs': {'enable_thinking': True}},
)

# llm = ChatOpenAI(
#     model='deepseek-chat',
#     temperature=0.8,
#     api_key="sk-YBLKX7wJEJ8wuFUWGujP8Iw13GneZhEZDCVaz6Rivv9ps9wy",
#     base_url="https://xiaoai.plus/v1"
# )

# def get_weather(city: str) -> str:
#     """Get weather for a given city."""
#     return f"城市：{city}，今天的天气晴朗，气温在28摄氏度！"

graph = create_react_agent(
    llm,
    tools=[calculate4, runnable_tool, search_tool],
    prompt="你是一个智能助手"
)

# 以 graph.invoke 的方式执行智能体，不需要按照严格的目录结构、但是如果以 langgraph dev : 把智能体部署到Fast API,必须严格按照langgraph的目录结构来
# graph.invoke()        # 同步执行
# graph.ainvoke()       # 异步执行


# 执行智能体，不需要严格的目录结构
# for token, metadata in graph.stream(
#     input={"messages": [{"role": "user", "content": "计算一下(3 + 5) x 12的结果"}]},
#     stream_mode='messages-tuple'
# ):
#     print("Token", token)
#     print("Metadata", metadata)
#     print("\n")


# res = graph.invoke(
#     {"messages": [{"role": "user", "content": "给我一个小品的报幕词"}]},
#     config={"configurable": {"user_name": "laoxiao"}},
# )
#
# print(res['messages'][-1].content)