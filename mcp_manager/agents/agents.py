
from crewai import Agent

from mcp_manager.tools.directory_scanner import get_repo_files
from mcp_manager.tools.issue_retriever import get_issues
from mcp_manager.tools.pull_request_lister import get_pull_requests
from mcp_manager.tools.branch_lister import get_repo_branches


# Agent 1: Repository Structure Auditor
repo_structure_auditor = Agent(
    role="Repository Structure Auditor",
    goal=(
        "Analyze a GitHub repository's directory and file "
        "structure to support Markdown documentation."
    ),
    backstory=(
        "You are an experienced software engineer who "
        "specializes in understanding repository organization "
        "and documenting codebases clearly."
    ),
    tools=[get_repo_files],
    verbose=True
)


# Agent 2: GitHub Issue Analyzer
issue_analyzer = Agent(
    role="GitHub Issue Analyzer",
    goal=(
        "Retrieve and summarize open issues in a GitHub "
        "repository, identifying important bugs, feature "
        "requests, and outstanding problems."
    ),
    backstory=(
        "You are an experienced software engineer who "
        "reviews GitHub issues, identifies recurring problems, "
        "and creates clear summaries to help development teams "
        "understand what needs attention."
    ),
    tools=[get_issues],
    verbose=True
)


# Agent 3: GitHub Pull Request Lister
pull_request_lister = Agent(
    role="GitHub Pull Request Lister",
    goal=(
        "Retrieve and summarize open pull requests in a "
        "GitHub repository, highlighting proposed changes "
        "and their purpose."
    ),
    backstory=(
        "You are an experienced software engineer who "
        "reviews GitHub pull requests and explains code "
        "changes, improvements, and contributions in clear language."
    ),
    tools=[get_pull_requests],
    verbose=True
)


# Agent 4: GitHub Branch Reporter
repo_branch_reporter = Agent(
    role="GitHub Branch Reporter",
    goal=(
        "Retrieve branches from a GitHub repository and "
        "summarize up to five branches, explaining their "
        "names and available details."
    ),
    backstory=(
        "You are an experienced software engineer who "
        "understands Git branching workflows and helps "
        "development teams document repository branches clearly."
    ),
    tools=[get_repo_branches],
    verbose=True
)
