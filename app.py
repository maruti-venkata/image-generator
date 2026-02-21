import os
import urllib.parse

import anthropic
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
client = anthropic.Anthropic()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    word = (data or {}).get("word", "").strip()

    if not word:
        return jsonify({"error": "Please type a word first!"}), 400

    if len(word) > 50:
        return jsonify({"error": "That word is too long! Try a shorter one."}), 400

    # Use Claude to turn the word into a vivid, kid-friendly image prompt
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=120,
        system=(
            "You create short, joyful image prompts for a 6-year-old child. "
            "Always make prompts colorful, cute, magical, and completely child-safe. "
            "Reply with only the image prompt — no extra text."
        ),
        messages=[
            {
                "role": "user",
                "content": (
                    f'Create a fun image prompt about "{word}". '
                    "Make it bright, cheerful, and magical. "
                    "Under 25 words."
                ),
            }
        ],
    )

    prompt = response.content[0].text.strip()

    # Generate image via Pollinations.ai (free, no API key needed)
    encoded = urllib.parse.quote(prompt)
    image_url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        "?width=512&height=512&model=flux&nologo=true"
    )

    return jsonify({"prompt": prompt, "image_url": image_url})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
