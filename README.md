# Real-Time Cyber Threat Visualization Dashboard

A Flask-based real-time dashboard for visualizing and monitoring simulated cyber threats. This system features live data streaming, advanced filtering, and dynamic visualizations to support proactive threat detection workflows.

## Features

- Real-time cyber threat feed (auto-updating)
- Interactive bar chart showing threat severity
- Pie chart summarizing threat categories
- Filter threats by type and severity
- Searchable and paginated log table
- Download logs as CSV with one click
- Responsive dark-themed UI for seamless desktop use

## Project Structure

real-time-cyber-threat-dashboard/
├── app.py                   # Flask backend
├── simulate_threat.py       # Simulates random threats
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── templates/
│   └── dashboard.html       # Frontend UI template
├── static/
│   ├── css/
│   │   └── style.css        # Custom dashboard styles
│   └── js/
│       └── charts.js        # Chart rendering logic
└── threat_logs.csv          # Auto-generated threat logs

## Setup Instructions

# Step 1: Clone the repository
git clone https://github.com/Syed-Abdul-Mateen/real-time-cyber-threat-dashboard.git
cd real-time-cyber-threat-dashboard

# Step 2: (Optional) Create a virtual environment
python -m venv venv
# Activate the environment:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Start the Flask server
python app.py

# Step 5: Open the dashboard
# Visit in your browser:
http://127.0.0.1:5000

# Step 6: Run the threat simulation (in a new terminal)
python simulate_threat.py

## Export Logs

To export all logged threats, click the "Download CSV" button in the dashboard. The data will be saved to threat_logs.csv.

## Requirements

- Python 3.7 or higher
- Flask
- requests
- Bootstrap 5 (via CDN)
- Chart.js (via CDN)

# To install dependencies manually
pip install flask requests

## License

This project is licensed under the MIT License.
