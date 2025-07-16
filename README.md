# Real-Time Cyber Threat Visualization Dashboard

This project is a Flask-based real-time dashboard to visualize and monitor simulated cyber threats. It includes live data feeds, search, filters, CSV export, and interactive charts using Chart.js.

## Features

- Real-time live threat feed
- Bar chart for threat severity
- Pie chart for threat types
- Filtering by type and severity
- Searchable log table
- Auto-refresh threat data (without reloading charts)
- Export threats as CSV
- Modern dark-themed responsive UI

## Project Structure
```
real-time-cyber-threat-dashboard/
├── app.py                   # Flask backend
├── simulate_threat.py       # Threat simulation script
├── requirements.txt         # Python dependencies
├── README.md
├── templates/
│   └── dashboard.html       # Main UI template
├── static/
│   ├── css/
│   │   └── style.css        # Dashboard styling
│   └── js/
│       └── charts.js        # Optional JS code
└── threat_logs.csv          # Exported threat data
```
## Setup Instructions

# 1. Clone the repository
git clone https://github.com/Syed-Abdul-Mateen/real-time-cyber-threat-dashboard.git
cd real-time-cyber-threat-dashboard

# 2. (Optional) Create a virtual environment
python -m venv venv
# Activate:
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask server
python app.py

# 5. Open the dashboard
# Visit: http://127.0.0.1:5000 in your browser

# 6. Start the threat simulation (in a new terminal)
python simulate_threat.py

## Export Logs

Click the "Download CSV" button in the dashboard to download all logged threats to `threat_logs.csv`.

## Requirements

- Python 3.7+
- Flask
- requests
- Bootstrap 5 (CDN)
- Chart.js (CDN)

To install dependencies manually:

pip install flask requests

## License

This project is licensed under the MIT License.
