from flask import Flask, request, jsonify
import painpoint, audience, swipe, calendar_tool

app = Flask(__name__)

@app.route('/generate-pain-point', methods=['POST'])
def generate_pain_point():
    data = request.json
    result = painpoint.run_painpoint(data.get('niche'))
    return jsonify({'result': result})

@app.route('/generate-audience-insight', methods=['POST'])
def generate_audience_insight():
    data = request.json
    result = audience.run_audience_insight(data.get('niche'))
    return jsonify({'result': result})

@app.route('/generate-swipe-copy', methods=['POST'])
def generate_swipe_copy():
    data = request.json
    result = swipe.run_swipe_copy(data.get('offer'))
    return jsonify({'result': result})

@app.route('/generate-content-calendar', methods=['POST'])
def generate_content_calendar():
    data = request.json
    result = calendar_tool.run_content_calendar(data.get('niche'))
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
