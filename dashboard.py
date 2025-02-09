# dashboard.py
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Import the global simulated_data from simulate.py.
from simulate import simulated_data

class IoTDashboard:
    def __init__(self, root):
        """
        Initialize the dashboard with labels showing sensor readings and a matplotlib plot for recent heart rate data.
        """
        self.root = root
        self.root.title("Real-Time IoT Healthcare Monitoring Dashboard")
        self.root.geometry("800x600")
        
        # Top frame for sensor data display.
        self.top_frame = ttk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Create labels for each sensor reading.
        self.hr_label = ttk.Label(self.top_frame, text="Heart Rate: -- bpm", font=("Arial", 12))
        self.hr_label.pack(side=tk.LEFT, padx=10)
        
        self.bp_label = ttk.Label(self.top_frame, text="Blood Pressure: -- / -- mmHg", font=("Arial", 12))
        self.bp_label.pack(side=tk.LEFT, padx=10)
        
        self.ox_label = ttk.Label(self.top_frame, text="Oxygen Saturation: -- %", font=("Arial", 12))
        self.ox_label.pack(side=tk.LEFT, padx=10)
        
        self.temp_label = ttk.Label(self.top_frame, text="Temperature: -- °C", font=("Arial", 12))
        self.temp_label.pack(side=tk.LEFT, padx=10)
        
        # Bottom frame for the matplotlib plot.
        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create a matplotlib Figure and add a subplot.
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Recent Heart Rate (bpm)")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Heart Rate")
        self.line, = self.ax.plot([], [], marker='o')  # Initialize an empty plot.
        
        # Embed the matplotlib Figure in the Tkinter frame.
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.bottom_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Start the periodic dashboard updates.
        self.update_dashboard()
    
    def update_dashboard(self):
        """
        Update sensor labels and the heart rate plot.
        This method is scheduled to run every second.
        """
        # Check if there is any data available.
        if simulated_data["timestamp"]:
            # Get the latest sensor readings.
            current_hr = simulated_data["heart_rate"][-1]
            current_systolic = simulated_data["systolic_bp"][-1]
            current_diastolic = simulated_data["diastolic_bp"][-1]
            current_ox = simulated_data["oxygen_sat"][-1]
            current_temp = simulated_data["temperature"][-1]
            
            # Update labels.
            self.hr_label.config(text=f"Heart Rate: {current_hr} bpm")
            self.bp_label.config(text=f"Blood Pressure: {current_systolic} / {current_diastolic} mmHg")
            self.ox_label.config(text=f"Oxygen Saturation: {current_ox} %")
            self.temp_label.config(text=f"Temperature: {current_temp} °C")
            
            # For plotting, display only the last 10 data points.
            data_length = len(simulated_data["timestamp"])
            last_10 = slice(max(0, data_length - 10), data_length)
            times = simulated_data["timestamp"][last_10]
            hr_values = simulated_data["heart_rate"][last_10]
            
            # Clear the current plot and re-plot the data.
            self.ax.clear()
            self.ax.plot(times, hr_values, marker='o', linestyle='-')
            self.ax.set_title("Recent Heart Rate (bpm)")
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Heart Rate")
            self.ax.tick_params(axis='x', rotation=45)
            self.fig.tight_layout()
            self.canvas.draw()
        
        # Schedule this method to run again after 1000 ms (1 second).
        self.root.after(1000, self.update_dashboard)
