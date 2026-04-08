# Smart Notepad MCP

A simple AI-powered note-taking assistant using MCP and LangChain.

## Features
- Add, read, search, and delete notes
- Natural language search for flexible note retrieval
- Safe deletion with Python confirmation

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
````

3. Create `.env` with your OpenRouter API key:

   ```
   OPENROUTER_API_KEY=your_key_here
   ```
4. Ensure `notes.json` exists:

   ```json
   []
   ```

## Run

```bash
python3 client.py
```

## Usage

* Type normal instructions like:

  * `Save a note about meeting with Fahad`
  * `Show all notes`
  * `Delete the meeting with Fahad`

* Confirm deletion when prompted (`y` / `n`)
