from flask import Flask, request, jsonify
import openai
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

app = Flask(__name__)

# Google Sheets API setup
SERVICE_ACCOUNT_FILE = 'brandvision-service-account.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_social_calendar(business_name, niche, user_email):
    prompt = f"""
You are an elite AI branding strategist.

For the business "{business_name}" in the "{niche}" niche, create a 30-day social media content calendar.

For each day, provide:
- Post idea/topic
- Recommended format
- Suggested emotional tone
- Headline or caption
- 3–5 hashtags
- Visual cue
- CTA
- Best time to post

Break into 4 weeks:
- Week 1: Awareness
- Week 2: Trust
- Week 3: Engagement
- Week 4: Soft Sell

Top: Include brand voice reminder + audience pain points addressed.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )

    full_text = response["choices"][0]["message"]["content"]
    lines = full_text.split("\n")
    rows = []
    current_day = {}

    for line in lines:
        line = line.strip()
        if line.lower().startswith("day "):
            if current_day:
                rows.append(current_day)
            current_day = {"Day": line}
        elif "topic" in line.lower():
            current_day["Post Topic"] = line.split(":")[-1].strip()
        elif "format" in line.lower():
            current_day["Format"] = line.split(":")[-1].strip()
        elif "tone" in line.lower():
            current_day["Tone"] = line.split(":")[-1].strip()
        elif "caption" in line.lower():
            current_day["Caption"] = line.split(":")[-1].strip()
        elif "hashtag" in line.lower():
            current_day["Hashtags"] = line.split(":")[-1].strip()
        elif "visual" in line.lower():
            current_day["Visual Cue"] = line.split(":")[-1].strip()
        elif "cta" in line.lower():
            current_day["CTA"] = line.split(":")[-1].strip()
        elif "time" in line.lower():
            current_day["Best Time"] = line.split(":")[-1].strip()

    if current_day:
        rows.append(current_day)

    df = pd.DataFrame(rows)
    sheet_title = f"{business_name} Calendar - {datetime.today().strftime('%Y-%m-%d')}"
    spreadsheet = gc.create(sheet_title)
    worksheet = spreadsheet.sheet1
    worksheet.update([df.columns.tolist()] + df.fillna("").values.tolist())
    spreadsheet.share(user_email, perm_type='user', role='writer')

    return spreadsheet.url

@app.route("/generate-calendar", methods=["POST"])
def generate_calendar():
    data = request.get_json()
    business_name = data.get("business_name", "Your Brand")
    niche = data.get("niche", "Branding")
    user_email = data.get("user_email", "test@brandvision.ai")
    link = run_social_calendar(business_name, niche, user_email)
    return jsonify({"sheet_link": link})
