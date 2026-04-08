from mcp.server.fastmcp import FastMCP
import json
import os
import mcp

macp = FastMCP("Smart Notepad")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")

@mcp.tool()
def add_note(title: str, content: str) -> str:
    with open("NOTES_FILE", "r") as f:
        notes = json.load(f)

    new_note = {
        "tile" : title,
        "content" : content
    }

    notes.append(new_note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

    return f"Note '{title}' saved successfully!"

@mcp.tool()
def get_notes() ->str:
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    if not notes:
        return "No Notes Found!"
    
    output = ""

    for i, note in enumerate(notes, start=1):
        output += f"{i}. {note['titel']} : {note['content']}\n"

    return output

if __name__ == "__main__":
    mcp.run(transport="stdio")

