# Multi-AI-Query-Tool
Different AI chatbots have their own strengths and weaknesses. This tool gives you a side-by-side comparison of two AI chatbots - Claude and Gemini. Usage of this tool requires API keys for each respective chatbot.
# Multi-AI Query Tool

Send one prompt to **Claude** (Anthropic) and **Gemini** (Google) simultaneously and compare their responses side by side.

---

## Features

- Side-by-side responses from Claude and Gemini
- Full markdown rendering (headers, code blocks, tables, bullet points)
- Multi-turn conversation — follow-up questions maintain context
- Enter to send, Shift+Enter for new line
- Copy responses as plain text
- Recent prompt history
- API keys saved locally in your browser

---

## Requirements

- **Python 3.x** — download from [python.org](https://python.org). During install, tick **"Add Python to PATH"**.
- **API keys** (separate from chat subscriptions):
  - Claude: [console.anthropic.com](https://console.anthropic.com) → API Keys → Create key. Starts with `sk-ant-`. Requires a credit card (very cheap per use).
  - Gemini: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) → Create API key. Starts with `AIza`. Free tier available, no card needed.

---

## Setup

1. Make sure all 3 files are in the same folder:
   - `multi-ai.html`
   - `server.py`
   - `Launch Multi-AI.bat`

2. Double-click **`Launch Multi-AI.bat`**

3. A minimized window appears in your taskbar (the local server). Leave it running.

4. Your browser opens automatically to `localhost:8731/multi-ai.html`

5. Click **⚙ API Keys** and enter your Claude and/or Gemini API keys. They're saved automatically — you only need to do this once per computer.

> ⚠️ Never open `multi-ai.html` by double-clicking it directly. Claude won't work that way. Always use the .bat launcher.

---

## How to use

- Type your prompt and press **Enter** to send (or click **Send to Both**)
- Use **Shift+Enter** to add a new line without sending
- The conversation remembers context — you can ask follow-up questions
- Click **New conversation** to start fresh
- Recent prompts appear at the bottom of the page for quick reuse

---

## Stopping the server

Right-click the minimized taskbar window and close it, or find `python.exe` in Task Manager and end it.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `invalid x-api-key` | Claude key is wrong. Generate a new one at console.anthropic.com |
| `API key not valid` | Gemini key is wrong. Generate a new one at aistudio.google.com/app/apikey |
| `model not found` | Change the model in the ⚙ dropdown |
| Page won't load | Check taskbar for server window. If missing, relaunch the .bat. Then go to `localhost:8731/multi-ai.html` manually |

---

## Sharing with others

1. Zip all 3 files together
2. Upload the zip to Google Drive (Gmail blocks .bat/.py attachments)
3. Share the Google Drive link

Recipients will need Python installed and their own API keys.
