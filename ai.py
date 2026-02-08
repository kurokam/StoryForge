import os
import asyncio
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_story(kind: str):
    try:
        system = (
            "You are StoryForge AI. Create a viral 15-second YouTube Shorts script. "
            "Return structured output with: HOOK, SCENE, TWIST, CAPCUT_PROMPT, TAGS. "
            "Language: Turkish. Style based on kind."
        )

        user = f"Create a viral {kind} short story for faceless anime-style video."

        # OpenAI client sync çalışır → async içinde thread'e atalım
        resp = await asyncio.to_thread(
            client.chat.completions.create,
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            temperature=0.9,
            timeout=30
        )

        return resp.choices[0].message.content

    except Exception as e:
        return f"❌ AI hata verdi:\n{e}"
