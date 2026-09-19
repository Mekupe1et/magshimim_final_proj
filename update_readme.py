#Not a serious part of the project!!!!
import os
import re
from pathlib import Path

# Files and folders to exclude from the tree
IGNORE_SET = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".ipynb_checkpoints",
    ".DS_Store",
    ".vscode",
    ".idea",
    "update_tree.py",  # Exclude this script itself if desired
}

README_PATH = "README.md"


def build_tree(dir_path: Path, prefix: str = "") -> list[str]:
    """Recursively generates tree lines with correct Unicode connectors."""
    lines = []

    # Get entries, filter out ignored items, and sort (directories first, then files)
    entries = [e for e in dir_path.iterdir() if e.name not in IGNORE_SET]
    entries.sort(key=lambda x: (x.is_file(), x.name.lower()))

    total = len(entries)
    for index, entry in enumerate(entries):
        is_last = index == total - 1
        connector = "└── " if is_last else "├── "

        # Append '/' to directory names for clarity
        display_name = f"{entry.name}/" if entry.is_dir() else entry.name
        lines.append(f"{prefix}{connector}{display_name}")

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            lines.extend(build_tree(entry, prefix + extension))

    return lines


def update_readme_tree():
    root = Path(".")
    root_name = root.resolve().name

    # Generate tree starting with root directory
    tree_lines = [f"{root_name}/"] + build_tree(root)
    tree_content = "\n".join(tree_lines)
    formatted_block = f"```text\n{tree_content}\n```"

    readme_file = Path(README_PATH)
    if not readme_file.exists():
        print(f"Error: Could not find {README_PATH}")
        return

    try:
        content = readme_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = readme_file.read_text(encoding="utf-16")
        except UnicodeDecodeError:
            content = readme_file.read_text(encoding="utf-8-sig")
    # Regex target: ## Directory Structure followed by the ```text ... ``` block
    pattern = r"(## Directory Structure\s*\n\s*)```text[\s\S]*?```"

    if re.search(pattern, content):
        new_content = re.sub(pattern, rf"\1{formatted_block}", content)
        readme_file.write_text(new_content, encoding="utf-8")
        print("Successfully updated the tree in README.md!")
    else:
        print(
            "Error: Could not match '## Directory Structure' block in README.md."
        )


if __name__ == "__main__":
    update_readme_tree()