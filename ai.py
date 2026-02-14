import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


async def generate_story(kind: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are StoryForge AI. Create a viral YouTube Shorts horror story in Turkish.\n"
                    "Return ONLY in this exact format (no extra text):\n\n"
                    "BASLIK:\n"
                    "<Merak uyandiran kisa baslik>\n\n"
                    "ACIKLAMA:\n"
                    "<2-3 cumlelik aciklama, izleyiciyi yoruma cagir>\n\n"
                    "SAHNELER (CapCut Prompt):\n"
                    "1. (0-3sn): <gercekci sinematik goruntu promptu, vertical 9:16, ultra realistic, cinematic lighting, 4k>\n"
                    "2. (3-6sn): <gercekci sinematik goruntu promptu, vertical 9:16, ultra realistic, cinematic lighting, 4k>\n"
                    "3. (6-9sn): <gercekci sinematik goruntu promptu, vertical 9:16, ultra realistic, cinematic lighting, 4k>\n"
                    "4. (9-12sn): <gercekci sinematik goruntu promptu, vertical 9:16, ultra realistic, cinematic lighting, 4k>\n"
                    "5. (12-15sn): <gercekci sinematik goruntu promptu, vertical 9:16, ultra realistic, cinematic lighting, 4k>\n\n"
                    "ETIKETLER:\n"
                    "<virgulle ayrilmis en populer YouTube Shorts etiketleri>"
                )
            },
            {
                "role": "user",
                "content": f"Konu: {kind}. Anime degil, gercekci karanlik korku hikayesi yaz."
            }
        ],
        "temperature": 0.9,
        "max_tokens": 400
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ AI hata verdi:\n{str(e)}"