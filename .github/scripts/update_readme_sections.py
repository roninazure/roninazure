import re
import datetime
import random

# Paths to the external data sources
NEURAL_DIAG_PATH = "../external/CodexDaemon/diagnostics/neural-diagnostics.md"
CLUE_BANK_PATH = "../external/project-darc/.github/assets/clue_bank.txt"
README_PATH = "README.md"

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def replace_section(content, marker, replacement):
    return re.sub(
        rf"<!-- START: {marker} -->.*?<!-- END: {marker} -->",
        f"<!-- START: {marker} -->\n{replacement}\n<!-- END: {marker} -->",
        content,
        flags=re.DOTALL
    )

def get_random_clue():
    clues = load_file(CLUE_BANK_PATH).strip().splitlines()
    return random.choice([c for c in clues if c.strip() and not c.startswith("#")])

def main():
    readme = load_file(README_PATH)
    diagnostics = load_file(NEURAL_DIAG_PATH).strip()
    clue = get_random_clue().strip()

    # Replace sections
    readme = replace_section(readme, "CODEX_PULSE", diagnostics)
    readme = replace_section(readme, "DAILY_CLUE", f"> `{clue}`")

    write_file(README_PATH, readme)

if __name__ == "__main__":
    main()
