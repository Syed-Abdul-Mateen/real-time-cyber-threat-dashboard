import requests
import random
import time
from datetime import datetime

# Target URL of your Flask app
url = 'http://127.0.0.1:5000/submit'

# Sample threats to simulate
threat_types = ['DDoS', 'Phishing', 'Malware', 'SQL Injection', 'Brute Force']
severities = ['low', 'medium', 'high']  # now all lowercase
descriptions = [
    'Suspicious login attempt detected',
    'Malicious payload detected in network packet',
    'Multiple failed login attempts from same IP',
    'SQL injection pattern detected',
    'Excessive bandwidth usage detected'
]

while True:
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'type': random.choice(threat_types),
        'severity': random.choice(severities),
        'description': random.choice(descriptions)
    }

    try:
        res = requests.post(url, json=data)
        print(f"[+] Sent: {data} - Status: {res.status_code}")
    except Exception as e:
        print(f"[!] Error sending data: {e}")

    time.sleep(1)  # Send one threat per second
