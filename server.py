from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("Smart Notepad")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")


# Core function: ensure storage file exists
def ensure_notes_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f)


# Tool 1: Save note
@mcp.tool()
def add_note(title: str, content: str) -> str:
    ensure_notes_file()

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    new_note = {
        "title": title,
        "content": content
    }

    notes.append(new_note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

    return f"Note '{title}' saved successfully!"


# Tool 2: Read all notes
@mcp.tool()
def get_notes() -> str:
    ensure_notes_file()

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    if not notes:
        return "No notes found!"

    output = ""

    for i, note in enumerate(notes, start=1):
        output += f"{i}. {note['title']}: {note['content']}\n"

    return output


# Tool 3: Search notes using natural language query
@mcp.tool()
def search_note(query: str) -> str:
    ensure_notes_file()

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    query = query.lower()
    matches = []

    for note in notes:
        title = note["title"].lower()
        content = note["content"].lower()

        if query in title or query in content:
            matches.append(note)

    if not matches:
        return "NOT_FOUND"

    return json.dumps(matches)


# Tool 4: Delete note by exact matched title
@mcp.tool()
def delete_note(title: str) -> str:
    ensure_notes_file()

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    updated_notes = [
        note for note in notes
        if note["title"].lower() != title.lower()
    ]

    if len(updated_notes) == len(notes):
        return "Note not found."

    with open(NOTES_FILE, "w") as f:
        json.dump(updated_notes, f, indent=2)

    return f"Note '{title}' deleted successfully!"


if __name__ == "__main__":
    mcp.run(transport="stdio")