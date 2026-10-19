# Agentic GitHub Workflow with CrewAI and MCP

An AI-powered multi-agent workflow that integrates **CrewAI, GitHub MCP Server, Django, and OpenAI** to automate GitHub repository analysis and generate structured documentation.

## Overview

This project demonstrates how AI agents can collaborate to analyze GitHub repositories, retrieve repository information, and produce documentation using the **Model Context Protocol (MCP)**.

It combines CrewAI's multi-agent orchestration with GitHub MCP tools and a Django-based web interface.

## Key Features

- **Repository Structure Analysis:** Explore repository directories and files.
- **GitHub Issue Retrieval:** Fetch and summarize repository issues.
- **Pull Request Analysis:** Retrieve pull request information.
- **Branch Listing:** Identify repository branches.
- **AI-Powered Documentation:** Generate structured Markdown reports from repository data.
- **Multi-Agent Orchestration:** Coordinate AI agents and tasks through CrewAI.
- **Django Web Interface:** Run repository analysis through a web application.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CrewAI | AI agent orchestration |
| GitHub MCP Server | GitHub repository tool integration |
| OpenAI API | LLM-powered analysis and generation |
| Django | Backend framework and web interface |
| GitHub API | Repository metadata and operations |
| Markdown | Generated documentation |

## Architecture

```text
User
  |
  v
Django Web Interface
  |
  v
CrewAI Workflow
  |
  +-- Repository Structure Task
  |
  +-- GitHub Issues Task
  |
  +-- Pull Requests Task
  |
  +-- Branch Analysis Task
  |
  v
GitHub MCP Server Tools
  |
  v
GitHub Repository Data
  |
  v
AI-Generated Markdown Documentation
```

## Project Structure

```text
mcp_integration/
|
|-- manage.py
|-- mcp_integration/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|
|-- mcp_manager/
|   |-- agents/
|   |   |-- agents.py
|   |
|   |-- crews/
|   |   |-- crew.py
|   |
|   |-- tasks/
|   |   |-- tasks.py
|   |
|   |-- tools/
|   |   |-- directory_scanner.py
|   |   |-- issue_retriever.py
|   |   |-- pull_request_lister.py
|   |   |-- branch_lister.py
|   |
|   |-- templates/
|   |-- views.py
|   |-- urls.py
|
|-- generated_docs/
|   |-- repo_structure.md
|   |-- report_issues.md
|   |-- report_pull_requests.md
|   |-- branches.md
|   |-- summary.md
|
|-- .gitignore
```

## How It Works

1. A user provides a GitHub repository owner and repository name.
2. Django receives the request and starts the workflow.
3. CrewAI coordinates agents and tasks.
4. Custom tools communicate with GitHub through the MCP integration.
5. Repository structure, issues, pull requests, and branches are retrieved.
6. AI agents process the information and generate Markdown documentation.
7. Results are saved and made available through the application.

## Local Setup

### Prerequisites

- Python
- Git
- GitHub account and Personal Access Token
- OpenAI API key
- GitHub MCP Server

### Environment Variables

Create a `.env` file in the project directory and configure the required credentials:

```env
OPENAI_API_KEY=your_openai_api_key
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
```

Never commit real API keys or access tokens to GitHub.

### Start the Django Application

After installing and configuring the project's dependencies, run:

```bash
python manage.py runserver
```

Open the local address shown in the terminal to access the Django application.

## Example Generated Outputs

The `generated_docs/` directory contains Markdown reports produced by the workflow:

- `repo_structure.md` — Repository structure
- `report_issues.md` — GitHub issue report
- `report_pull_requests.md` — Pull request report
- `branches.md` — Repository branch information
- `summary.md` — Generated repository summary

## Concepts Demonstrated

- AI agents and multi-agent workflows
- CrewAI task orchestration
- Model Context Protocol (MCP)
- LLM tool calling
- GitHub integration
- Django backend development
- Environment variable management
- Automated documentation generation
