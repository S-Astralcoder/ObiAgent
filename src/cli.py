# External
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown
# Internal
from src.agent import obi_agent
from src.vector_embedding.embedding import VaultEmbeddingEngine
from src.share import client, model


class AgentCLI:
    def __init__(self) -> None:
        self.console = Console()
        self.model = model
        self.client = client
        self.vault_embedding =  VaultEmbeddingEngine(client=client, model=model)
        self.vault_embedding.load_vault_data_to_vector_database(mode="passive")

    def start_agent_cli(self):
        self.console.print(f"[green]{'='*10}Welcome to ObiAgent CLI{'='*10}")
        while True:
            message = Prompt.ask("[blue]Let's Chat[bold white]", default="exit")
            if message.lower().strip() == "exit":
                return
            if message.lower().strip() == "$load":
                self.vault_embedding.load_vault_data_to_vector_database(mode="active")
                continue
            response = obi_agent.run_agent(message=message)
            self.console.print('[purple]ObiAgent[white] >')
            self.console.print(Markdown(response))
