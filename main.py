# pip install -qU langchain "langchain[openai]"
import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY1"),
    base_url=os.getenv("OPENAI_BASE_URL"),  # URL personalizada
    model="gpt-4o-mini",
)

agent = create_agent(
    ## model="openai:gpt-4o-mini",
    model=model,    
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)