import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_social_calendar(business_name, niche, user_email):
    prompt = f"""
You are an elite AI branding strategist.

For the business "{business_name}" in the "{niche}" niche, create a 30-day social media content calendar.

For each day, provide:
- Post idea/topic
- Recommended format (Reel, carousel, story, long-form post)
- Suggested emotional tone (e.g., funny, inspiring, authoritative, personal)
- Example headline or caption
- 3–5 relevant hashtags
- Visual cue (what to show in the post)
- Audience engagement prompt or CTA (e.g., 'Ask your audience a question')
- Best time to post

Also, break the 30 days into:
- Week 1: Build Awareness
- Week 2: Build Trust
- Week 3: Drive Engagement
- Week 4: Soft Sell or Launch

At the top, include:
- Brand voice reminder (1–2 lines)
- Summary of the audience’s top emotional pain points (and how this calendar addresses them)

Format clearly, with bold section headings and numbered days, for easy copy-paste.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )

    return response["choices"][0]["message"]["content"]
