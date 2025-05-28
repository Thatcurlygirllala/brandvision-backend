import openai

def run_social_calendar(business_name, niche, user_email):
    prompt = f"""
You are an AI social strategist.

Business: {business_name}
Niche: {niche}
Plan: Premium (30 days)

Generate a 30-day social content calendar:
- Short-form videos
- Long-form posts
- Best posting times
- Pain point hooks
- CTA prompts
- Bonus: AI Brand Audit Score (1-100) + feedback

Format clearly for easy reading.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response["choices"][0]["message"]["content"]
