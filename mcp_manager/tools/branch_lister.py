# Task 17: Build the Branch Lister Agent

from mcp_manager.utils import mcp_tool
from langchain.tools import StructuredTool


def list_branches(owner: str, repo: str) -> list:
    """
    Retrieve branches from a GitHub repository.
    """
    result = mcp_tool([
        "tools",
        "list_branches",
        "--owner", owner,
        "--repo", repo
    ])

    if isinstance(result, list):
        return result

    return []


get_repo_branches = StructuredTool.from_function(
    func=list_branches,
    name="get_repo_branches",
    description=(
        "Retrieves branches from a GitHub repository. "
        "Requires the GitHub repository owner and repository name."
    )
)


