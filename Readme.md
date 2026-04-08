# Smart Notepad MCP

A simple AI-powered note-taking assistant using MCP and LangChain.

## Features

- Add, read, search, and delete notes
- Natural language search for flexible note retrieval
- Safe deletion with confirmation prompt

## Setup

1. Clone the repo
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Create `.env` with your OpenRouter API key:
```python
OPENROUTER_API_KEY = YOUR_KEY_HERE
or
Your_API_key_provider = YOUR_KEY_HERE
```
And change the ` api_key=os.getenv("Your_API_key_provider").strip()`

4. Ensure `notes.json` exists:
```json
   []
```

## Run

```bash
python3 client.py
```

## Usage

Type natural language instructions like:

- `Save a note about meeting with Fahad`
- `Show all notes`
- `Delete the meeting with Fahad`

Confirm deletion when prompted (`y` / `n`)
