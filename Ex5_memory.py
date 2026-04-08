from typing import TypedDict, Annotated
import operator
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

# api key config
load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY").strip()

if not api_key:
    raise ValueError("API key not found in the directory or the key is not valid Or expired!")


# 1 - connect the LLM

llm = ChatOpenAI(
    model = 'minimax/minimax-m2.5:free',
    base_url ="https://openrouter.ai/api/v1",
    api_key = api_key,
    temperature = 0.7,
)