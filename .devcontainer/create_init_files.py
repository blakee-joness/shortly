import os
import sys


def run_hook():
    """
    This hook creates __init__.py files in all directories containing Python files.
    """
    new_files = []
    exclude_dirs = ["shortly"]  # add manually if needed.

    # Get all directories containing a Python file
    dirs_with_py = set()
    for root, _, files in os.walk("."):
        if any(fname.endswith(".py") for fname in files if "./frontend" not in root):
            dirs_with_py.add(root)

    # Iterate over the directories, excluding the ones in exclude_dirs
    for dir_path in dirs_with_py:
        dir_name = os.path.basename(dir_path)
        if dir_name not in exclude_dirs and not dir_name.startswith("."):
            init_path = os.path.join(dir_path, "__init__.py")
            if not os.path.exists(init_path):
                # Create __init__.py if it doesn't exist
                new_files.append(init_path)
                with open(init_path, "a", encoding="utf-8"):
                    pass

    if len(new_files) > 0:
        files = ", \n - ".join(new_files)
        sys.exit(
            f"Please stage the following newly created __init__.py files: \n - {files}"
        )


if __name__ == "__main__":
    run_hook()
