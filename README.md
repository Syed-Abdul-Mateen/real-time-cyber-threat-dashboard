# Real-Time Cyber Threat Visualization Dashboard

This project is a real-time dashboard built with Flask that simulates and displays cybersecurity threats dynamically. It provides alerts such as suspicious logins, malware activity, and network attacks using simulated data refreshed every few seconds.

---

## Project Structure

```
Real-Time Cyber Threat Visualization Dashboard/
│
├── app.py                   # Flask backend and simulation logic
├── requirements.txt         # Project dependencies
│
└── templates/
    └── index.html           # HTML dashboard UI
```

---

## Requirements

- Python 3.7 or higher
- pip (Python package manager)

---

## Setup Instructions

### 1. Install Python

Download from https://www.python.org/downloads/  
Ensure you select **"Add Python to PATH"** during installation.

---

### 2. Navigate to Project Directory

```bash
cd "D:\Projects\Real-Time Cyber Threat Visualization Dashboard"
```

---

### 3. (Optional) Create Virtual Environment

```bash
python -m venv cyber-env
cyber-env\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Flask App

```bash
python app.py
```

You should see:

```
* Running on http://127.0.0.1:5000
```

---

### 6. View Dashboard

Open your browser and go to:

```
http://127.0.0.1:5000
```

The dashboard updates every few seconds with simulated threat data.

---

## Customization Ideas

- Integrate real security logs from firewalls or servers
- Connect with SIEM tools (e.g., Splunk, ELK)
- Display alerts by severity or type
- Add user login or admin control

---

## Real-World Use Cases

- Educational cybersecurity simulations
- Prototypes for Security Operations Centers (SOC)
- Internal dashboards for network teams
- Training and demonstration environments

---

## License

MIT License — free for use, modification, and distribution.
