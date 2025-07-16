# Real-Time Cyber Threat Visualization Dashboard

A Flask-based real-time monitoring system for visualizing simulated cyber threats with dynamic analytics, advanced filtering, and auto-refreshing visualizations.

## Key Features

- Real-time cyber threat updates without page reloads
- Live threat log table with search and filters
- Pie chart (threat types) and bar chart (severity levels)
- Custom dark-themed UI with responsive layout
- Export logs to CSV with a single click

## Project Structure

real-time-cyber-threat-dashboard/
├── app.py                   # Flask backend server
├── simulate_threat.py       # Random cyber threat generator
├── requirements.txt         # Required Python packages
├── README.md                # Project documentation
├── threat_logs.csv          # Auto-generated threat logs
├── templates/
│   └── dashboard.html       # HTML layout and data binding
├── static/
│   ├── css/
│   │   └── style.css        # Custom dark UI styles
│   └── js/
│       └── charts.js        # JavaScript to render Chart.js visuals

## Setup Instructions

# Step 1: Clone the repository
git clone https://github.com/Syed-Abdul-Mateen/real-time-cyber-threat-dashboard.git
cd real-time-cyber-threat-dashboard

# Step 2: (Optional) Create a virtual environment
python -m venv venv

# Activate the environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Start the Flask server
python app.py

# Step 5: Open the dashboard in your browser
http://127.0.0.1:5000

# Step 6: Run the threat simulation in another terminal
python simulate_threat.py

## Export Logs

To export all logged threats, click the "Download CSV" button in the dashboard. The data will be saved to threat_logs.csv.

## Requirements

- Python 3.7 or higher
- Flask
- requests

# To install dependencies manually
pip install flask requests

## License

This project is licensed under the MIT License.
