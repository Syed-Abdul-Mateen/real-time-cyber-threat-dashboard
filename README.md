# Real-Time Cyber Threat Visualization Dashboard

A Flask-based real-time dashboard for visualizing and monitoring simulated cyber threats. This system features live data streaming, advanced filtering, auto-refreshing visualizations, and dark UI.

## Key Features

- Real-time threat feed with auto-update
- Interactive pie and bar charts (Chart.js)
- Filter threats by type and severity
- Searchable and responsive log table
- Export threat logs as CSV
- Responsive dark-themed UI with Bootstrap

## Project Structure

real-time-cyber-threat-dashboard/
├── app.py                   # Flask server (main app)
├── simulate_threat.py       # Sends simulated threats to the server
├── requirements.txt         # Python dependencies
├── README.md                # Documentation
├── threat_logs.csv          # CSV log (auto-generated)
├── templates/
│   └── dashboard.html       # UI layout with Jinja2 and Bootstrap
├── static/
│   ├── css/
│   │   └── style.css        # Custom dark theme styles
│   └── js/
│       └── charts.js        # Dynamic chart rendering with Chart.js

## Setup Instructions

# Step 1: Clone the repository
git clone https://github.com/Syed-Abdul-Mateen/real-time-cyber-threat-dashboard.git
cd real-time-cyber-threat-dashboard

# Step 2: (Optional) Create and activate a virtual environment
python -m venv venv

# Activate the environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Step 3: Install required dependencies
pip install -r requirements.txt

# Step 4: Start the Flask web server
python app.py

# Step 5: Open your browser and visit the dashboard
http://127.0.0.1:5000

## Running the Threat Simulator

To simulate live cyber threat data, you must run the `simulate_threat.py` script **in a separate terminal window or tab** while the Flask server is running.

# Open a new terminal (do not close the previous one)
# Activate the virtual environment again if necessary

# Then run the simulator
python simulate_threat.py

# This script will continuously send random cyber threat data every second to your Flask app
# You will see new threats appearing in the dashboard in real time

## Export Logs

Click the **Download CSV** button in the dashboard UI to download all logged threats to `threat_logs.csv`.

## Requirements

- Python 3.7 or above
- Flask
- requests

# If not using requirements.txt:
pip install flask requests

## License

This project is licensed under the MIT License.
