
from crewai import Crew, Process

from mcp_manager.agents.agents import (
    repo_structure_auditor,
    issue_analyzer,
    pull_request_lister,
    repo_branch_reporter
)

from mcp_manager.tasks.tasks import (
    analyze_repo_structure_task,
    get_issue_tasks,
    list_pull_requests_tasks,
    list_branches_tasks
)


def build_crew(owner, repo):
    tasks = []

    # Task 1: Repository structure
    tasks.extend(analyze_repo_structure_task(owner, repo))

    # Task 2: GitHub open issues
    tasks.extend(get_issue_tasks(owner, repo))

    # Task 3: GitHub pull requests
    tasks.append(list_pull_requests_tasks(owner, repo))

    # Task 4: GitHub branches
    tasks.append(list_branches_tasks(owner, repo))

    crew = Crew(
        agents=[
            repo_structure_auditor,
            issue_analyzer,
            pull_request_lister,
            repo_branch_reporter
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        cache=True
    )

    return crew
