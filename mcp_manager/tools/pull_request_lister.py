# Task 15: Build the Pull Request Lister Agent

# Task 15: Build the Pull Request Lister Agent

from mcp_manager.utils import mcp_tool
from langchain.tools import StructuredTool


def list_pull_requests(owner: str, repo: str) -> list:
    """
    Retrieve pull requests from a GitHub repository.
    """
    result = mcp_tool([
        "tools",
        "list_pull_requests",
        "--owner", owner,
        "--repo", repo,
        "--state", "open"
    ])

    if isinstance(result, list):
        return result

    return []


get_pull_requests = StructuredTool.from_function(
    func=list_pull_requests,
    name="list_pull_requests",
    description=(
        "Retrieves open pull requests from a GitHub repository. "
        "Requires the GitHub repository owner and repository name."
    )
)
