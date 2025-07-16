from flask import Flask, render_template, request, jsonify, send_file
import csv
import os
from datetime import datetime

app = Flask(__name__)
threats = []  # In-memory storage


@app.route('/')
def dashboard():
    return render_template('dashboard.html', threats=threats)


@app.route('/submit', methods=['POST'])
def submit_threat():
    data = request.get_json()

    # Add timestamp if not present
    if 'time' not in data:
        data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Normalize severity
    if 'severity' in data:
        data['severity'] = data['severity'].lower()

    threats.append(data)
    return jsonify({'status': 'success'}), 200


@app.route('/export')
def export_csv():
    filename = 'threat_logs.csv'
    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, mode='w', newline='') as csvfile:
        fieldnames = ['time', 'type', 'severity', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for threat in threats:
            writer.writerow(threat)

    return send_file(filepath, as_attachment=True)


@app.route('/api/threats')
def get_threats():
    return jsonify(threats)


if __name__ == '__main__':
    app.run(debug=True)
