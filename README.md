# ObiAgent: Intelligent Obsidian Vault Management

> [!ABSTRACT] Overview
> **ObiAgent** is an intelligent, agent-based assistant designed to streamline the management and navigation of your Obsidian vault. By leveraging AI-driven semantic search and an agentic architecture, it allows for seamless interaction with your knowledge base, enabling complex task execution and automated organization.

---

## 🛠 Project Status
> [!WARNING] Early-Stage MVP
> This project is currently in active development. Features are being implemented and refined rapidly. Please use with caution and **ensure your vault is backed up** before performing automated operations.

| Feature | Status |
| :--- | :--- |
| **Error Handling** | ❌ Not implemented |
| **Performance** | ⚠️ Not optimized |

---

## ✨ Key Capabilities
*   **Semantic Search**: Advanced retrieval system that understands context, allowing you to find notes beyond simple keyword matching.
*   **Agentic Intelligence**: Powered by Gemini, the agent reasons through complex vault tasks and executes operations autonomously.
*   **Dual-Search Strategy**: Intelligent fallback mechanism that switches between semantic search and manual filesystem traversal for comprehensive coverage.
*   **Vector Infrastructure**: Utilizes Qdrant for high-performance vector embeddings and efficient data retrieval.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have [uv](https://github.com/astral-sh/uv) installed to manage the project dependencies.

### Installation & Setup
1.  **Clone the repository** and navigate into the project directory.
2.  **Sync dependencies** using `uv`:
    ```bash
    uv sync
    ```
3.  **Configuration**: Populate your `.env` file with the required API keys.

### Execution
Run the agent using the `uv` environment:
```bash
uv run python main.py
```

## 💡 How to Use ObiAgent

Once you have initialized the agent, you can interact with it through natural language commands in your terminal. ObiAgent is designed to perform operations directly on your Obsidian vault files.

### Common Patterns
- **File Management**: You can request tasks such as "Create a note about project XYZ" or "Update the task list in the work-notes file."
- **Retrieval**: Use queries like "Find all notes related to my meeting last week" to leverage semantic search.
- **Vault Maintenance**: Ask the agent to list folder contents or summarize specific files.

### Special Commands
While the agent supports natural language processing, you can use these special commands to manage the interaction session directly:

- `/load-vault`: Force a re-indexing (active reload) of your vault data into the vector database.
- `/exit`: Terminate the current session and close the agent.

### Workflow Example
1. Launch the agent using `uv run python main.py`.
2. When prompted (`Let's Chat`), type your query or a special command.
3. The agent will process your request, perform a semantic search if necessary, and output the result.

> [!IMPORTANT]
> The agent performs direct filesystem operations. Always ensure you have a backup of your vault before performing bulk edits or deletions.

---

## 🏗 Technical Stack
- **Core Agent**: Custom Nexus framework integration.
- **LLM Engine**: Gemini (`gemini-3.1-flash-lite`).
- **Storage**: Qdrant (Vector Database).
- **Dependency Management**: `uv`.
