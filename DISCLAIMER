# Disclaimer & Important Information

Please read this before using the Multi-AI Query Tool.

---

## API keys are not the same as a subscription

If you pay for Claude.ai Pro or Gemini Advanced, **those subscriptions do not cover API usage.** The API is a completely separate billing system.

- **Claude API** requires a credit card connected to your Anthropic account at [console.anthropic.com](https://console.anthropic.com). You are charged per message based on how many tokens (words) are processed.
- **Gemini API** has a free tier with usage limits. Paid usage is billed through your Google account at [aistudio.google.com](https://aistudio.google.com).

You will not be charged just for having a key — only when you actually send messages.

---

## API pricing (approximate)

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

---

## Multi-turn conversations cost more

Every time you send a follow-up in the same conversation, **the entire conversation history is sent to the API again** so the AI has context. A 10-message conversation costs significantly more than 10 separate single questions.

**To keep costs low:** use **+ New** to start a fresh chat for each unrelated question. Only continue the same conversation when you need the AI to remember what was said earlier.

Alternatively, turn on **Single-turn mode** (see below) to automatically send every message fresh with no history.

---

## How to use the controls

Three toggle pills appear just above the input box.

### Claude toggle (orange)

- **On (default):** Claude is active and will respond to every message.
- **Off:** Claude is skipped entirely. Only Gemini responds. Use this to save money or when you only care about one AI's answer.

Click the pill to switch. The dot glows orange when active.

### Gemini toggle (blue)

- **On (default):** Gemini is active and will respond to every message.
- **Off:** Gemini is skipped entirely. Only Claude responds.

Click the pill to switch. The dot glows blue when active.

> You can disable one or both. If both are disabled, the tool will warn you before sending.

### Single-turn mode (yellow when on)

- **Off (default):** Conversation history is kept. The AI remembers everything said earlier in the current chat — useful for follow-up questions.
- **On:** Each message is sent as a standalone question with no history. The AI treats every message as a fresh start.

**When to use single-turn mode:**
- You're asking unrelated questions back to back and don't need context
- You want to minimize API costs
- You're sharing a conversation and want each answer to be self-contained

Switching this mode clears any existing history automatically.

---

## Your API keys are sensitive — treat them like passwords

- Your keys are stored only in your browser's local storage on your own computer.
- They are never sent anywhere except directly to Anthropic (for Claude) and Google (for Gemini).
- **Do not share your keys.** Anyone with your key can make API calls charged to your account.
- If you share this tool with others, make sure your keys are not pre-filled before you send it.
- You can revoke and regenerate keys at any time:
  - Claude: [console.anthropic.com](https://console.anthropic.com) → API Keys
  - Gemini: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## Setting spending limits (recommended)

To avoid unexpected charges, set a monthly spending limit on your Claude account:

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Navigate to **Billing → Usage limits**
3. Set a monthly cap (e.g. $5) — Anthropic will stop API access once the limit is reached

Google's free-tier limits for Gemini naturally cap usage without a credit card.

