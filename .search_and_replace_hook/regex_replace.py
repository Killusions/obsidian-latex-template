#!/usr/bin/env python
import os
import re
import sys

# Define the list of search and replace patterns
PATTERNS = [
    (
        re.compile(r'\n "metadata":\s*\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'),
        '\n	"metadata": {\n  "kernelspec": {\n   "display_name": ".venv",\n   "language": "python",\n   "name": "python3"\n  },\n  "language_info": {\n   "codemirror_mode": {\n    "name": "ipython",\n    "version": 3\n   },\n   "file_extension": ".py",\n   "mimetype": "text/x-python",\n   "name": "python",\n   "nbconvert_exporter": "python",\n   "pygments_lexer": "ipython3",\n   "version": "3.12.6"\n  }\n}',
    ),
    (re.compile(r'"execution_count": (?:\d+|null)'), '"execution_count": 1'),
    (re.compile(r"/Users/[^/\n:]+(/?)"), "~\\1"),
    (re.compile(r"/home/[^/\n:]+(/?)"), "~\\1"),
    (re.compile(r"/home/[^/\n:]+(/?)"), "~\\1"),
    (re.compile(r"/?[cC]:/Users/[^/\n:]+(/?)"), "~/"),
    (re.compile(r"/?[cC]:\\{1,2}Users\\{1,2}[^\\\n:]+\\{1,2}(?!\\?n\")"), "SAR_HOOK_TEMP_WINDOWS_PATH~/"),
    (re.compile(r"/?[cC]:\\{1,2}Users\\{1,2}[^\\\n:]+"), "~"),
    (re.compile(r"SAR_HOOK_TEMP_WINDOWS_PATH~/([^\\\n:]+)\\{1,2}(?!\\?n\")"), "SAR_HOOK_TEMP_WINDOWS_PATH~/\\1/"),
    (re.compile(r"SAR_HOOK_TEMP_WINDOWS_PATH"), ""),
    (re.compile(r"/?C:\\{1,2}Users\\{1,2}(?:[^\\\n:]*\\{1,2})*(?!\\?n\")"), "SAR_HOOK_REMOVE_WINDOWS_PATH"),
    (re.compile(r"\.\.\\{1,2}(?:[^\\\n:]*\\{1,2})+(?!\\?n\")"), "SAR_HOOK_REMOVE_WINDOWS_PATH"),
    (re.compile(r"~/AppData/Roaming/"), "~/"),
]

# Define a pattern to recognize paths within the current git repository
# Get the path of the current git repository
GIT_REPO_PATH = os.popen("git rev-parse --show-toplevel").read().strip()
# Get cleaned path to the git repository (with os.path) and convert to forward slashes
GIT_REPO_PATH = os.path.normpath(GIT_REPO_PATH).replace("\\", "/")
# Get relative path to the user root directory
USER_HOME = os.path.expanduser("~").replace("\\", "/")
# Replace the user home directory with ~
GIT_REPO_PATH = GIT_REPO_PATH.replace(USER_HOME, "~")
# Strip trailing slashes
GIT_REPO_PATH = GIT_REPO_PATH.rstrip("/")
# Create a pattern to match the git repository path
REPO_PATH_PATTERN = re.compile(r"~?/?" + re.escape(GIT_REPO_PATH) + r"(?:/[^/\n:]*)*")

# Define the pattern to fail the hook if found
FAIL_PATTERN = re.compile(r"SAR_HOOK_REMOVE_WINDOWS_PATH")


def replace_in_file(filename):
    """Read a file and replace text according to the patterns. Return True if changes were made."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content
    for search_pattern, replacement in PATTERNS:
        # Apply the replacement pattern until no more changes are detected
        while True:
            previous_content = new_content
            new_content = search_pattern.sub(replacement, new_content)
            if new_content == previous_content:
                break

    # Replace the git repository path with a relative path, run a lambda function to make the path relative (using os.path)
    new_content = REPO_PATH_PATTERN.sub(
        lambda x: re.sub(r"\\u([0-9A-Fa-f]{4})", "SAR_TEMP_BACKSLASHu\\1", os.path.relpath(os.path.realpath(os.path.expanduser(x.group(0))), os.path.dirname(os.path.realpath(os.path.expanduser(filename)))).replace("\\n", "SAR_HOOK_TEMP_ESCAPED_NEWLINE"))
        .replace("\\", "/")
        .replace("SAR_TEMP_BACKSLASH", "\\")
        .replace("SAR_HOOK_TEMP_ESCAPED_NEWLINE", "\\n"),
        new_content,
    )

    if new_content != content:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(new_content)
        return True

    return False


def check_fail_pattern(filename):
    """Check if the fail pattern is present in the file. Return True if found."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    if FAIL_PATTERN.search(content):
        return True
    return False


def get_files_to_check():
    """Get a list of files to check, skipping those in directories starting with a dot."""
    files = sys.argv[1:]  # Get file list from command-line arguments
    print(f"Files received for checking: {files}")  # Debugging output

    # Filter out files or directories starting with a dot
    files_to_check = [file for file in files if not any(part.startswith(".") for part in file.split(os.sep))]
    print(f"Filtered files to check: {files_to_check}")  # Debugging output

    return files_to_check


def main():
    """Main function to execute the pre-commit hook logic."""
    files_to_check = get_files_to_check()

    for filename in files_to_check:
        if filename.endswith((".json", ".py", ".ipynb", ".mojo", ".🔥", ".txt", ".js", ".ts", ".yml", ".yaml")):  # Adjust file types as needed
            replace_in_file(filename)

    # Check for the fail pattern
    for filename in files_to_check:
        if check_fail_pattern(filename):
            print(f"Error: The pattern '{FAIL_PATTERN.pattern}' was found in {filename}.")
            sys.exit(1)  # Fail the hook

    print("Pre-commit hook completed successfully.")
    sys.exit(0)  # Success


if __name__ == "__main__":
    main()
