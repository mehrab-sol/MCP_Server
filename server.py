from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("Smart Notepad")


NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")

# 1 - Tool
@mcp.tool(description="Save a note with title and content")
def add_note(title: str, content: str) -> str:
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    new_note = {
        "title" : title,
        "content" : content
    }

    notes.append(new_note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

    return f"Note '{title}' saved successfully!"



# 2 - Tool
@mcp.tool(description="Retrieve all saved notes")
def get_notes() ->str:
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    if not notes:
        return "No Notes Found!"
    
    output = ""

    for i, note in enumerate(notes, start=1):
        output += f"{i}. {note['title']} : {note['content']}\n"

    return output



# 3 - Tool
# @mcp.too(description="Delete Notes when user asked")


if __name__ == "__main__":
    mcp.run(transport="stdio")

