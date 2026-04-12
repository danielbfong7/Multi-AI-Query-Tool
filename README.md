# Multi-AI Query Tool

Send one prompt to **Claude** (Anthropic), **Gemini** (Google), and **ChatGPT** (OpenAI) simultaneously and compare their responses side by side.

---

## Features

- Side-by-side responses from Claude, Gemini, and ChatGPT
- Full markdown rendering (headers, code blocks, tables, bullet points)
- Multi-turn conversation — follow-up questions maintain context
- **Single-turn mode** — send each message fresh with no history (saves API cost)
- **Disable individual AIs** — run any combination of one, two, or all three
- **Image input** — attach an image and all enabled AIs will analyze it
- **Image generation** — dedicated tab to generate images with DALL-E (OpenAI) and Nano Banana (Google), side by side
- **Light / dark mode** toggle
- Side-by-side or **stacked layout** for responses
- Enter to send, Shift+Enter for new line
- Copy individual responses, or copy all visible responses at once (with formatting preserved)
- Chat history saved automatically in the sidebar, with **rename** and **delete** per chat
- **Search chats** — filter your saved chats by name instantly
- API keys saved locally in your browser — never sent anywhere except the AI APIs

---

## Files in this folder

| File | Purpose |
|------|---------|
| `multi-ai.html` | The main tool (open this via the launcher) |
| `server.py` | Local server that handles Claude and ChatGPT API calls |
| `Launch Multi-AI.bat` | Windows launcher — double-click to start everything |
| `Launch Multi-AI.command` | Mac launcher — double-click to start everything |
| `README.md` | This file |

---

## Requirements

- **Python 3.x** — download from [python.org](https://python.org).
  - Windows: during install, tick **"Add Python to PATH"**.
  - Mac: Python 3 is usually pre-installed. Check by running `python3 --version` in Terminal.
- **API keys** — separate from your chat subscriptions (see the Disclaimer section below):
  - Claude: [console.anthropic.com](https://console.anthropic.com) → API Keys → Create key. Starts with `sk-ant-`. Requires a credit card.
  - Gemini: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) → Create API key. Starts with `AIza`. Free tier available.
  - ChatGPT: [platform.openai.com/api-keys](https://platform.openai.com/api-keys) → Create new secret key. Starts with `sk-`. Requires a credit card.

---

## Setup

1. Make sure all files stay in the same folder.
2. Launch the tool:
   - **Windows:** double-click **`Launch Multi-AI.bat`**
   - **Mac:** double-click **`Launch Multi-AI.command`** (first time only: run `chmod +x "Launch Multi-AI.command"` in Terminal to make it executable)
3. A terminal/server window opens — leave it running.
4. Your browser opens automatically to `localhost:8731/multi-ai.html`
5. Click **API Keys** and enter your keys for Claude, Gemini, and/or ChatGPT. Saved automatically — you only need to do this once per computer.

> Never open `multi-ai.html` by double-clicking it directly. Claude won't work that way. Always use the launcher.

---

## How to use

- Type your prompt and press **Enter** to send (or **Shift+Enter** for a new line)
- Responses appear side by side with full formatting
- Use the **Copy** button on each response, or **Copy all / Copy both** to grab all visible responses at once
- Click **+ New** in the sidebar to start a fresh conversation
- Click any past chat in the sidebar to reload it
- **Rename** a chat by hovering over it in the sidebar and clicking ✎, then press Enter to save
- **Delete** a chat by hovering over it and clicking ✕ — you'll be asked to confirm first
- **Search chats** by typing in the search box at the top of the sidebar — results filter instantly

### Controls above the input box

The toggle pills just above the input box control how the tool behaves. Use **▲ Hide / ▼ Show** on the right to collapse them when not needed.

| Toggle | What it does |
|--------|-------------|
| **Claude** (orange) | Click to disable/enable Claude. |
| **Gemini** (blue) | Click to disable/enable Gemini. |
| **ChatGPT** (green) | Click to disable/enable ChatGPT. |
| **Single-turn mode** (amber when on) | Each message is sent without conversation history — lowest cost option. |
| **Stacked layout** (green when on) | Responses appear one above the other instead of side by side. |

---

## Stopping the server

- **Windows:** right-click the minimized taskbar window and close it, or find `python.exe` in Task Manager and end it.
- **Mac:** close the Terminal window that opened when you launched the tool.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `invalid x-api-key` | Claude key is wrong. Generate a new one at console.anthropic.com |
| `API key not valid` | Gemini key is wrong. Generate a new one at aistudio.google.com/app/apikey |
| `model not found` | Change the model in the model dropdown |
| Page won't load | Check that the server window is still open. If missing, relaunch the `.bat` (Windows) or `.command` (Mac). Then go to `localhost:8731/multi-ai.html` manually |
| Only one response showing | One AI is toggled off — click its pill above the input to re-enable it |

---

## Sharing with others

1. Zip all files together (multi-ai.html, server.py, Launch Multi-AI.bat, Launch Multi-AI.command)
2. Upload the zip to Google Drive (Gmail blocks .bat and .py attachments)
3. Share the Google Drive link

Recipients will need Python installed and their own API keys. Windows users use the `.bat`, Mac users use the `.command`.

---

## Disclaimer

### API keys are not the same as a subscription

If you pay for Claude.ai Pro, Gemini Advanced, or ChatGPT Plus, **those subscriptions do not cover API usage.** The API is a completely separate billing system.

- **Claude API** requires a credit card at [console.anthropic.com](https://console.anthropic.com). Charged per token.
- **Gemini API** has a free tier with usage limits. Paid usage billed through [aistudio.google.com](https://aistudio.google.com).
- **ChatGPT API** requires a credit card at [platform.openai.com](https://platform.openai.com). Charged per token.

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
| 2.0 Flash / 1.5 series | Older models, free tier available |

**ChatGPT (OpenAI):**

| Model | Notes |
|-------|-------|
| GPT-4o mini | ~$0.0006/1K output — cheapest |
| GPT-4o | ~$0.01/1K output |
| GPT-5 series | Most capable, most expensive |
| o1 / o3 (reasoning) | Significantly more expensive |

**Image generation (Image Gen tab):**

| Model | Cost per image |
|-------|---------------|
| GPT Image 1 mini | ~$0.005 |
| GPT Image 1 | ~$0.04 |
| GPT Image 1.5 | ~$0.04+ |
| Nano Banana (Google) | Varies — free tier may apply |

The token counts shown in each response (e.g. **30↑ 309↓**) tell you how many tokens were sent up (↑) and received down (↓). Multiply by the model's price to estimate cost.

### Multi-turn conversations cost more

Every time you send a follow-up in the same conversation, **the entire conversation history is sent to the API again** so the AI has context. A 10-message conversation costs significantly more than 10 separate single questions.

**To keep costs low:** use **+ New** to start a fresh chat for each unrelated question. Only continue the same conversation when you need the AI to remember what was said earlier. Alternatively, turn on **Single-turn mode** to automatically send every message fresh with no history.

### Your API keys are sensitive — treat them like passwords

- Your keys are stored only in your browser's local storage on your own computer.
- They are never sent anywhere except directly to the respective AI APIs.
- **Do not share your keys.** Anyone with your key can make API calls charged to your account.
- If you share this tool with others, make sure your keys are not pre-filled before you send it.
- Revoke and regenerate keys at any time: [console.anthropic.com](https://console.anthropic.com) (Claude), [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) (Gemini), [platform.openai.com/api-keys](https://platform.openai.com/api-keys) (ChatGPT).

### Setting a spending limit (recommended)

To avoid unexpected charges, set monthly spending limits:

- **Claude:** go to [console.anthropic.com](https://console.anthropic.com) → Billing → Usage limits → set a monthly cap (e.g. $5)
- **ChatGPT:** go to [platform.openai.com/account/limits](https://platform.openai.com/account/limits) → set a monthly budget
- **Gemini:** free-tier limits apply automatically; paid usage can be monitored at [aistudio.google.com](https://aistudio.google.com)
