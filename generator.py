# generator.py (OpenAI v1.x compatible)

import re
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_prompt(topic, tone, bullet_points):
    return f"""
    Create a LinkedIn post.

    Topic: {topic}
    Tone: {tone}
    Key Points: {bullet_points if bullet_points else 'N/A'}

    The post should be engaging, suitable for LinkedIn, and contain a call to action if appropriate.
    """

# generator.py

def beautify_post(text):
    """
    Beautifies the LinkedIn post by adding:
    - Line breaks after punctuation
    - Emojis for key terms
    - Extra space between sections (paragraphs)
    """
    text = re.sub(r"([.?!])\s+", r"\1\n\n", text)  # Add extra space after punctuation marks
    emoji_map = {
        "growth": "📈", "team": "👥", "leadership": "🧠",
        "success": "🏆", "challenge": "⚔️", "opportunity": "🚀",
        "learning": "📚", "grateful": "🙏", "excited": "🔥",
    }
    for word, emoji in emoji_map.items():
        text = re.sub(fr"\b{word}\b", f"{word} {emoji}", text, flags=re.IGNORECASE)

    # Add extra space before key takeaways or next sections
    text = re.sub(r"(key takeaways|lessons learned|what’s next)", r"\n👉 \1", text, flags=re.IGNORECASE)

    # Add a couple of newlines between paragraphs
    text = text.replace("\n", "\n")  # Ensure proper paragraph spacing

    return text.strip()


def generate_linkedin_post(topic, tone, bullet_points, beautify=False):
    prompt = create_prompt(topic, tone, bullet_points)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        post = response.choices[0].message.content.strip()
        return beautify_post(post) if beautify else post
    except Exception as e:
        return f"❌ Error: {e}"
