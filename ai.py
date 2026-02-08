import os
import httpx

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/responses"

async def generate_story(kind: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = (
        "You are StoryForge AI. Create a viral 15-second YouTube Shorts script in Turkish. "
        "Return structured output with: HOOK, SCENE, TWIST, CAPCUT_PROMPT, TAGS. "
        f"Theme: {kind}."
    )

    payload = {
        "model": "llama-3.1-8b-instant",
        "input": prompt,
        "temperature": 0.9,
        "max_output_tokens": 300
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(GROQ_URL, headers=headers, json=payload)
            if r.status_code != 200:
                return f"❌ Groq status={r.status_code}\n{r.text}"
            data = r.json()
            # responses API farklı döner:
            return data["output"][0]["content"][0]["text"]
    except Exception as e:
        return f"❌ İstek hatası: {e}"
