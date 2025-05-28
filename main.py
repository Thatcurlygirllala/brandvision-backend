from flask import Flask, request, jsonify
import combined_profiler, swipe, ai_social_calendar

app = Flask(__name__)

@app.route('/generate-combined-profiler', methods=['POST'])
def generate_combined_profiler():
    data = request.json
    result = combined_profiler.run_combined_profiler(
        data.get('niche'),
        data.get('audience'),
        data.get('product')
    )
    return jsonify({'result': result})

@app.route('/generate-swipe-copy', methods=['POST'])
def generate_swipe_copy():
    data = request.json
    result = swipe.run_swipe_copy(
        data.get('offer'),
        data.get('audience'),
        data.get('tone')
    )
    return jsonify({'result': result})

@app.route('/generate-social-calendar', methods=['POST'])
def generate_social_calendar():
    data = request.json
    result = ai_social_calendar.run_social_calendar(
        data.get('business_name'),
        data.get('niche'),
        data.get('user_email')
    )
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
