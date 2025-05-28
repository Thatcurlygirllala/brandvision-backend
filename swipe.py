import openai

def run_swipe_copy(offer, audience=None, tone="engaging and persuasive"):
    prompt = f"""
You are a swipe copy expert.

Offer: {offer}
Audience: {audience or 'general market'}
Tone: {tone}

Generate:
- 5 headlines
- 3 call-to-action lines
- 2 product hook statements

Format clearly and make it emotionally engaging.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response["choices"][0]["message"]["content"]
