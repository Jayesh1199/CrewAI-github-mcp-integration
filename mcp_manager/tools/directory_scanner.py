# Task 7: Create a Custom Tool to Analyze a Repository’s Structure

from mcp_manager.utils import mcp_tool
from langchain.tools import StructuredTool

def list_repo_files(owner: str, repo: str, path: str = "") -> list:
    """
    List files and folders in a GitHub repository.
    """
    result = mcp_tool([
        "tools",
        "get_file_contents",
        "--owner", owner,
        "--repo", repo,
        "--path", path or "/"
    ])

    if isinstance(result, list):
        return result

    return []


get_repo_files = StructuredTool.from_function(
    func=list_repo_files,
    name="get_repo_files",
    description="Lists files and folders in a GitHub repository. Requires the repository owner and name, with an optional directory path."
)


