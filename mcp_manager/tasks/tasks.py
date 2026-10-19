
from crewai import Task

from mcp_manager.agents.agents import (
    repo_structure_auditor,
    issue_analyzer,
    pull_request_lister,
    repo_branch_reporter
)

from mcp_manager.tools.directory_scanner import get_repo_files
from mcp_manager.tools.issue_retriever import get_issues
from mcp_manager.tools.pull_request_lister import get_pull_requests
from mcp_manager.tools.branch_lister import get_repo_branches


# Task 1: Analyze repository structure
def analyze_repo_structure_task(owner, repo):
    task = Task(
        description=(
            f"Analyze the GitHub repository {owner}/{repo}. "
            "Use the get_repo_files tool to retrieve the repository's "
            "files and directories. "
            "Generate a Markdown-formatted directory tree showing "
            "the repository structure. "
            "Include clickable GitHub links using "
            f"https://github.com/{owner}/{repo}/blob/main/ "
            "as the base URL for files on the main branch."
        ),
        expected_output=(
            "A well-structured Markdown document containing "
            "the repository's file and folder hierarchy, "
            "with clickable GitHub links to files."
        ),
        agent=repo_structure_auditor,
        tools=[get_repo_files],
        output_file="generated_docs/repo_structure.md"
    )
    return [task]


# Task 2: Analyze open GitHub issues
def get_issue_tasks(owner, repo):
    task = Task(
        description=(
            f"Analyze the open GitHub issues for {owner}/{repo}. "
            "Use the get_issues tool to retrieve open issues. "
            "Summarize them in Markdown. Categorize issues into "
            "bugs, feature requests, documentation, and improvements "
            "where appropriate. "
            "Recommend priorities and include GitHub issue links. "
            "If no open issues exist, state that clearly. "
            "Do not invent issues."
        ),
        expected_output=(
            "A Markdown report summarizing open GitHub issues, "
            "their categories, important problems, and priorities."
        ),
        agent=issue_analyzer,
        tools=[get_issues],
        output_file="generated_docs/report_issues.md"
    )
    return [task]


# Task 3: Analyze open pull requests
def list_pull_requests_tasks(owner, repo):
    task = Task(
        description=(
            f"Analyze the open pull requests for {owner}/{repo}. "
            "Use the list_pull_requests tool to retrieve pull requests. "
            "Summarize up to five of the most recently created "
            "open pull requests, ordered newest first. "
            "Include each PR's number, title, author, purpose, "
            "and clickable GitHub URL when available. "
            "If no open pull requests exist, state that clearly. "
            "Do not invent pull requests."
        ),
        expected_output=(
            "A Markdown summary of up to five recent open "
            "pull requests with their details and links."
        ),
        agent=pull_request_lister,
        tools=[get_pull_requests],
        output_file="generated_docs/report_pull_requests.md"
    )
    return task


# Task 4: Analyze repository branches
def list_branches_tasks(owner: str, repo: str):
    task = Task(
        description=(
            f"Retrieve GitHub branches for {owner}/{repo}. "
            "Use the get_repo_branches tool with the owner "
            "and repository name. "
            "Select up to five branches from the returned list. "
            "Generate a Markdown report containing each branch's "
            "name and available information, such as commit SHA. "
            "Include links to the branches when possible. "
            "Do not guess what a branch does based only on its name. "
            "If no branches are returned, state that clearly. "
            "Do not invent branch information."
        ),
        expected_output=(
            "A Markdown report listing up to five repository "
            "branches, including branch names, available "
            "commit details, and GitHub links."
        ),
        agent=repo_branch_reporter,
        tools=[get_repo_branches],
        output_file="generated_docs/branches.md"
    )
    return task
