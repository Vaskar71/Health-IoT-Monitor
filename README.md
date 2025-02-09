# Real-Time IoT Healthcare Monitoring Dashboard

https://github.com/user-attachments/assets/8e5afddb-b697-49cf-936f-af568714849f

## Overview
This project is a desktop-based real-time IoT monitoring dashboard for healthcare applications. It simulates healthcare sensor data, processes it in real-time, and visualizes trends for continuous monitoring. The application is built using Python and Tkinter for the user interface, with Matplotlib for data visualization.

## Project Architecture
- **Data Simulation Module:** Generates real-time healthcare data (heart rate, blood pressure, oxygen saturation, temperature) at regular intervals.
- **Dashboard Interface:** A Tkinter-based GUI that displays real-time sensor readings and plots trends using Matplotlib.
- **Data Processing & Storage:** Processes incoming sensor data and logs it to a CSV file for future analysis.
- **Multi-threading:** Ensures smooth real-time updates without freezing the GUI by handling data simulation in a separate thread.

## Tech Stack
- **Python:** Core language for implementation.
- **Tkinter:** GUI framework for the desktop application.
- **Matplotlib:** Used for plotting real-time sensor trends.
- **Pandas:** Handles data storage and processing.
- **Threading:** Ensures real-time updates without UI lag.

## How to Use
### Prerequisites
- Install Python (>=3.8)
- Install required dependencies:
  ```bash
  pip install matplotlib pandas
  ```

### Running the Application
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd iot-health-dashboard
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. The dashboard will launch, displaying real-time sensor data with graphical trends.

## Features
- Simulates real-time healthcare sensor data.
- Displays live sensor readings in a desktop GUI.
- Plots historical trends for better monitoring.
- Logs data to CSV for analysis.

## Future Enhancements
- Integration with real IoT devices.
- Cloud-based storage and analytics.
- Mobile application support for remote monitoring.

