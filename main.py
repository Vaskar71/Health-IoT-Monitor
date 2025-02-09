# main.py
import threading
import tkinter as tk
import pandas as pd

# Import the simulation function and globals.
from simulate import simulate_data, simulated_data, running
# Import the dashboard class.
from dashboard import IoTDashboard

def main():
    global running
    # Start the simulation in a separate daemon thread.
    simulation_thread = threading.Thread(target=simulate_data, daemon=True)
    simulation_thread.start()
    
    # Create the main Tkinter window.
    root = tk.Tk()
    app = IoTDashboard(root)
    
    # Define a function to handle a graceful exit.
    def on_closing():
        global running
        running = False  # Stop the simulation loop.
        root.destroy()   # Close the Tkinter window.
    
    # Bind the window close event.
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Start the Tkinter main loop.
    root.mainloop()
    
    # After closing the window, export the simulated data to a CSV file.
    df = pd.DataFrame(simulated_data)
    df.to_csv("simulated_health_data.csv", index=False)
    print("Simulated data saved to simulated_health_data.csv")

if __name__ == "__main__":
    main()
