# Multi-AI Query Tool

Send one prompt to **Claude** (Anthropic) and **Gemini** (Google) simultaneously and compare their responses side by side.

---

## Features

- Side-by-side responses from Claude and Gemini
- Full markdown rendering (headers, code blocks, tables, bullet points)
- Multi-turn conversation — follow-up questions maintain context
- **Single-turn mode** — send each message fresh with no history (saves API cost)
- **Disable individual AIs** — run only Claude or only Gemini to cut costs
- **Image input** — attach an image and both AIs will analyze it
- **Light / dark mode** toggle
- Side-by-side or **stacked layout** for responses
- Enter to send, Shift+Enter for new line
- Copy individual or both responses (with formatting preserved)
- Chat history saved automatically in the sidebar, with **rename** and **delete** per chat
- **Search chats** — filter your saved chats by name instantly
- API keys saved locally in your browser — never sent anywhere except the AI APIs

---

## Files in this folder

| File | Purpose |
|------|---------|
| `multi-ai.html` | The main tool (open this via the .bat launcher) |
| `server.py` | Local server that handles Claude API calls |
| `Launch Multi-AI.bat` | Double-click this to start everything |
| `README.md` | This file |

---

## Requirements

- **Python 3.x** — download from [python.org](https://python.org). During install, tick **"Add Python to PATH"**.
- **API keys** — separate from your chat subscriptions (see the Disclaimer section below):
  - Claude: [console.anthropic.com](https://console.anthropic.com) → API Keys → Create key. Starts with `sk-ant-`. Requires a credit card.
  - Gemini: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) → Create API key. Starts with `AIza`. Free tier available.

---

## Setup

1. Make sure all files stay in the same folder.
2. Double-click **`Launch Multi-AI.bat`**
3. A minimized window appears in your taskbar (the local server). Leave it running.
4. Your browser opens automatically to `localhost:8731/multi-ai.html`
5. Click **⚙ API Keys** and enter your Claude and/or Gemini API keys. Saved automatically — you only need to do this once per computer.

> ⚠️ Never open `multi-ai.html` by double-clicking it directly. Claude won't work that way. Always use the .bat launcher.

---

## How to use

- Type your prompt and press **Enter** to send (or **Shift+Enter** for a new line)
- Responses appear side by side with full formatting
- Use the **Copy** button on each response, or **Copy both** to grab both at once
- Click **+ New** in the sidebar to start a fresh conversation
- Click any past chat in the sidebar to reload it
- **Rename** a chat by hovering over it in the sidebar and clicking ✎, then press Enter to save
- **Delete** a chat by hovering over it and clicking ✕ — you'll be asked to confirm first
- **Search chats** by typing in the search box at the top of the sidebar — results filter instantly

### Controls above the input box

The toggle pills just above the input box control how the tool behaves. Use **▲ Hide / ▼ Show** on the right to collapse them when not needed.

| Toggle | What it does |
|--------|-------------|
| **Claude** (orange) | Click to disable/enable Claude. When off, only Gemini runs and its card takes the full width. |
| **Gemini** (blue) | Click to disable/enable Gemini. When off, only Claude runs. |
| **Single-turn mode** (amber when on) | Each message is sent without conversation history — lowest cost option. |
| **Stacked layout** (green when on) | Responses appear one above the other instead of side by side. |

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
| Claude disabled message | Claude toggle is off — click the Claude pill above the input to re-enable |
| Gemini disabled message | Gemini toggle is off — click the Gemini pill above the input to re-enable |

---

## Sharing with others

1. Zip all files together (multi-ai.html, server.py, Launch Multi-AI.bat, README.md)
2. Upload the zip to Google Drive (Gmail blocks .bat and .py attachments)
3. Share the Google Drive link

Recipients will need Python installed and their own API keys.

---

## ⚠ Disclaimer

### API keys are not the same as a subscription

If you pay for Claude.ai Pro or Gemini Advanced, **those subscriptions do not cover API usage.** The API is a completely separate billing system.

- **Claude API** requires a credit card connected to your Anthropic account at [console.anthropic.com](https://console.anthropic.com). You are charged per message based on how many tokens (words) are processed.
- **Gemini API** has a free tier with usage limits. Paid usage is billed through your Google account at [aistudio.google.com](https://aistudio.google.com).

You will not be charged just for having a key — only when you actually send messages.

### API pricing (approximate)

Costs are per 1,000 tokens. Roughly 1 token ≈ 1 word.

**Claude (Anthropic):**

| Model | Cost per 1K output tokens |
|-------|--------------------------|
| Haiku 4.5 | ~$0.001 (cheapest) |
| Sonnet 4.6 | ~$0.005 |
| Opus 4.6 | ~$0.015 (most expensive) |

**Gemini (Google):**

| Model | Notes |
|-------|-------|
| 2.5 Flash | Free tier available — best for everyday use |
| 2.5 Pro | Free tier with lower limits |
| 3.1 Flash Lite | Paid only |
| 3.1 Pro | ~$0.002/1K input, ~$0.012/1K output |

The token counts shown in each response (e.g. **30↑ 309↓**) tell you how many tokens were sent up (↑) and received down (↓). Multiply by the model's price to estimate cost.

### Multi-turn conversations cost more

Every time you send a follow-up in the same conversation, **the entire conversation history is sent to the API again** so the AI has context. A 10-message conversation costs significantly more than 10 separate single questions.

**To keep costs low:** use **+ New** to start a fresh chat for each unrelated question. Only continue the same conversation when you need the AI to remember what was said earlier. Alternatively, turn on **Single-turn mode** to automatically send every message fresh with no history.

### Your API keys are sensitive — treat them like passwords

- Your keys are stored only in your browser's local storage on your own computer.
- They are never sent anywhere except directly to Anthropic (for Claude) and Google (for Gemini).
- **Do not share your keys.** Anyone with your key can make API calls charged to your account.
- If you share this tool wit
