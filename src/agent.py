from nexus.agent import Agent
from nexus.model import ModelBase


from src.tools import tool_registry



instruction = """You are a Professional Obsidian Vault Manager Agent. You are responsible for help user with tasks related to their obsidian vault."""


obi_agent =Agent(model_base=ModelBase(model="gemini/gemini-3.1-flash-lite"), instruction=instruction, tool_registry=tool_registry)