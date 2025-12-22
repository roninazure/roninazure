# update_readme_timestamp.py
import re
from datetime import datetime

README_PATH = "README.md"

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_timestamp(content):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return re.sub(
        r"(<!-- AUTO_TIMESTAMP_START -->)(.*?)(<!-- AUTO_TIMESTAMP_END -->)",
        rf"\1{timestamp}\3",
        content,
        flags=re.DOTALL
    )

def main():
    readme = load_file(README_PATH)
    updated = update_timestamp(readme)
    write_file(README_PATH, updated)

if __name__ == "__main__":
    main()
