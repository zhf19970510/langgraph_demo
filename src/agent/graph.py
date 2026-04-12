from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# 本地私有化部署的大模型
llm = ChatOpenAI(
    model='qwen3-8b',
    temperature=0.8,
    api_key='xx',
    base_url="http://localhost:6006/v1",
    extra_body={'chat_template_kwargs': {'enable_thinking': False}},
)

# llm = ChatOpenAI(
#     model='deepseek-chat',
#     temperature=0.8,
#     api_key="sk-YBLKX7wJEJ8wuFUWGujP8Iw13GneZhEZDCVaz6Rivv9ps9wy",
#     base_url="https://xiaoai.plus/v1"
# )

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"城市：{city}，今天的天气晴朗，气温在28摄氏度！"

graph = create_react_agent(
    llm,
    tools=[get_weather],
    prompt="你是一个智能助手"
)