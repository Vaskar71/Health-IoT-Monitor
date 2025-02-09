# simulate.py
import time
import random

# Global dictionary to store simulated sensor data over time.
# Each key holds a list of values collected over time.
simulated_data = {
    "timestamp": [],
    "heart_rate": [],
    "systolic_bp": [],
    "diastolic_bp": [],
    "oxygen_sat": [],
    "temperature": []
}

# A flag to control the simulation loop.
running = True

def simulate_data():
    """
    Simulate healthcare sensor data.
    This function runs in a loop (every 1 second) and appends simulated data to the global dictionary.
    Data includes:
      - Heart rate: 60-100 bpm.
      - Systolic BP: 90-140 mmHg.
      - Diastolic BP: 60-90 mmHg.
      - Oxygen Saturation: 95-100 %.
      - Temperature: 36.0-37.5 °C.
    """
    global simulated_data, running
    while running:
        # Current time as a string (HH:MM:SS)
        current_time = time.strftime("%H:%M:%S")
        # Generate simulated values
        heart_rate = random.randint(60, 100)
        systolic_bp = random.randint(90, 140)
        diastolic_bp = random.randint(60, 90)
        oxygen_sat = random.randint(95, 100)
        temperature = round(random.uniform(36.0, 37.5), 1)
        
        # Append each new reading into the simulated_data dictionary.
        simulated_data["timestamp"].append(current_time)
        simulated_data["heart_rate"].append(heart_rate)
        simulated_data["systolic_bp"].append(systolic_bp)
        simulated_data["diastolic_bp"].append(diastolic_bp)
        simulated_data["oxygen_sat"].append(oxygen_sat)
        simulated_data["temperature"].append(temperature)
        
        # Wait for 1 second before generating the next set of data.
        time.sleep(1)
