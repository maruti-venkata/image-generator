# Magic Picture Maker ✨

A fun web app for kids — type any word and get a matching AI-generated picture!

**Slack integration is now ready!** You can generate images directly from Slack.

Built for a 6-year-old: colorful animated UI, quick-pick word chips, and large vivid images.

**Slack integration is now ready!** You can generate images directly from Slack.

## How it works

1. Your child types a word (or taps a chip like 🦄 unicorn)
2. [Claude](https://anthropic.com) turns the word into a cheerful, child-safe image prompt
3. [Pollinations.ai](https://pollinations.ai) generates a 512×512 image from that prompt
4. The picture appears on screen — ready to enjoy!

## Prerequisites

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

## Running locally

```bash
# 1. Clone the repo
git clone <repo-url>
cd image-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Anthropic API key
export ANTHROPIC_API_KEY=your_key_here

# 4. Start the app
python app.py
```

Then open **http://localhost:5000** in your browser.

## Project structure

```
image-generator/
├── app.py                  # Flask backend — Claude prompt + image URL generation
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Kid-friendly frontend (HTML/CSS/JS)
```

## Tech stack

| Layer    | Technology |
|----------|------------|
| Backend  | Python / Flask |
| AI prompt| Anthropic Claude (`claude-opus-4-6`) |
| Images   | Pollinations.ai (free, no extra key) |
| Frontend | Vanilla HTML + CSS + JS |
