# External
from dotenv import load_dotenv


# Internal
from src.cli import AgentCLI


load_dotenv()

agent_cli = AgentCLI()

agent_cli.start_agent_cli()
