# Task 13: Build an Issue Analyzer Agent

from mcp_manager.utils import mcp_tool
from langchain.tools import StructuredTool


def get_open_issues(owner: str, repo: str) -> list:
    """
    Retrieve open issues from a GitHub repository.
    """
    result = mcp_tool([
        "tools",
        "list_issues",
        "--owner", owner,
        "--repo", repo,
        "--state", "open"
    ])

    if isinstance(result, list):
        return result

    return []


get_issues = StructuredTool.from_function(
    func=get_open_issues,
    name="get_issues",
    description=(
        "Retrieves open GitHub issues from a repository. "
        "Requires the GitHub repository owner and repository name."
    )
)

