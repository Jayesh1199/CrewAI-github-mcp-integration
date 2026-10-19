
import os
import markdown

from django.shortcuts import render
from django.conf import settings

from mcp_manager.crews.crew import build_crew


# API keys loaded from Django settings
GITHUB_TOKEN = getattr(
    settings, "GITHUB_PERSONAL_ACCESS_TOKEN", None
)

OPENAI_API_KEY = getattr(
    settings, "OPENAI_API_KEY", None
)


# Extract owner and repository from GitHub URL
def extract_owner_repo(repo_url):
    parts = repo_url.strip().split("/")

    if len(parts) >= 5 and parts[2] == "github.com":
        owner = parts[3]
        repo_name = parts[4].removesuffix(".git")

        if owner and repo_name:
            return owner, repo_name

    raise ValueError("Invalid GitHub repository URL format.")


# Combine generated Markdown files
def combine_markdown_files(file_paths, output_path, owner, repo_name):
    combined_content = f"# Summary for {owner}/{repo_name}\n\n"

    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

                if (
                    lines
                    and lines[0].strip() == "```markdown"
                    and lines[-1].strip() == "```"
                ):
                    markdown_content = "".join(lines[1:-1]).strip()
                else:
                    markdown_content = "".join(lines).strip()

                combined_content += "\n\n---\n\n" + markdown_content

        except FileNotFoundError:
            print(f"Warning: File not found: {file_path}")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(combined_content.strip())

        print(f"Combined output saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"Error saving combined Markdown: {e}")
        return None


# Convert Markdown into HTML
def convert_markdown_to_html(markdown_file_path):
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()

        return markdown.markdown(
            markdown_text,
            extensions=["extra"]
        )

    except Exception as e:
        print(f"Error converting Markdown to HTML: {e}")
        return None


# Show the repository submission form
def documentation_interface(request):
    return render(
        request,
        "mcp_manager/documentation_interface.html"
    )


# Task 11: Generate documentation using CrewAI
def generate_documentation(request):

    if request.method != "POST":
        return render(
            request,
            "mcp_manager/documentation_interface.html",
            {"error": "Please submit a GitHub repository URL."}
        )

    repo_url = request.POST.get("repo_url", "").strip()

    try:
        # Step 1: Validate repository URL
        owner, repo_name = extract_owner_repo(repo_url)

        # Step 2: Verify OpenAI API key
        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is missing from Django settings."
            )

        # Step 3: Build CrewAI workflow
        crew = build_crew(owner, repo_name)

        # Step 4: Execute CrewAI agents and tasks
        crew.kickoff()

        # Step 5: Locate generated documentation
        output_dir = os.path.join(
            settings.BASE_DIR,
            "generated_docs"
        )

        file_paths = [
            os.path.join(output_dir, "repo_structure.md"),
            os.path.join(output_dir, "report_issues.md"),
            os.path.join(output_dir, "pull_requests.md"),
            os.path.join(output_dir, "branches.md")
        ]

        # Step 6: Combine Markdown files
        summary_path = os.path.join(
            output_dir,
            "summary.md"
        )

        os.makedirs(output_dir, exist_ok=True)

        combined_file = combine_markdown_files(
            file_paths,
            summary_path,
            owner,
            repo_name
        )

        if not combined_file:
            raise ValueError(
                "Failed to combine generated documentation."
            )

        # Step 7: Convert Markdown to HTML
        html_content = convert_markdown_to_html(
            combined_file
        )

        if html_content is None:
            raise ValueError(
                "Failed to convert documentation to HTML."
            )

        # Step 8: Display generated documentation
        return render(
            request,
            "mcp_manager/documentation_display.html",
            {
                "documentation": html_content,
                "owner": owner,
                "repo": repo_name
            }
        )

    except Exception as e:
        return render(
            request,
            "mcp_manager/documentation_interface.html",
            {
                "error": str(e),
                "repo_url": repo_url
            }
        )
