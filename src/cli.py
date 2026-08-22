# External
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown
# Internal
from src.agent import obi_agent

class AgentCLI:
    def __init__(self) -> None:
        self.console = Console() 

    def start_agent_cli(self):
        self.console.print(f"[green]{'='*10}Welcome to ObiAgent CLI{'='*10}")
        while True:
            message = Prompt.ask("[blue]Let's Chat[bold white]", default="exit")
            if message.lower().strip() == "exit":
                return
            response = obi_agent.run_agent(message=message)
            self.console.print('[purple]ObiAgent[white] >')
            self.console.print(Markdown(response))
