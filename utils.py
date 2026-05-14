import os


def save_to_file(content: str, filename: str) -> str:
    os.makedirs("output", exist_ok=True)

    filepath = os.path.join("output", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath
