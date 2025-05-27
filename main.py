
from flask import Flask, request, jsonify
from painpoint import run_painpoint
from audience import run_audience
from swipe import run_swipe
from calendar_tool import run_calendar

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'BrandVision API is live!'})

@app.route('/painpoint', methods=['POST'])
def painpoint():
    data = request.json
    result = run_painpoint(data['input'])
    return jsonify({'result': result})

@app.route('/audience', methods=['POST'])
def audience():
    data = request.json
    result = run_audience(data['input'])
    return jsonify({'result': result})

@app.route('/swipe', methods=['POST'])
def swipe():
    data = request.json
    result = run_swipe(data['input'])
    return jsonify({'result': result})

@app.route('/calendar', methods=['POST'])
def calendar():
    data = request.json
    result = run_calendar(data['input'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
