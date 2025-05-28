import openai

def run_combined_profiler(niche, audience=None, product=None):
    prompt = f"""
You are an elite AI strategist.

Niche: {niche}
Audience: {audience or 'general audience'}
Product: {product or 'general product'}

Step 1: Describe the audience persona (demographics, behaviors, emotional drivers).
Step 2: Identify top 5 emotional pain points (with emotional roots).
Step 3: Recommend marketing messages that calm pain + activate desires.
Step 4: Suggest product positioning + sales triggers to stand out.
Step 5: Provide emotional tone and messaging tips.

Format the output in clean sections.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response["choices"][0]["message"]["content"]
