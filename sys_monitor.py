# system_monitor.py
# A Python script to monitor and log system CPU and memory usage.
# To run this script, you first need to install the 'psutil' library:
# pip install psutil

import psutil
import time
import datetime
import csv
import os

# --- Configuration ---
LOG_INTERVAL_SECONDS = 5  # Time between logs in seconds
LOG_FILE_NAME = "system_performance_log.csv"

def get_performance_metrics():
    """
    Retrieves the current CPU and memory usage percentages.
    
    Returns:
        A tuple containing:
        - CPU usage percentage (float)
        - Memory usage percentage (float)
    """
    # Get CPU usage. The interval parameter is important to get a non-blocking,
    # meaningful reading over a short period.
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Get memory usage details
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    
    return cpu_percent, memory_percent

def setup_log_file():
    """
    Creates the log file and writes the header row if the file doesn't exist.
    """
    # Check if the file already exists to avoid writing the header multiple times
    file_exists = os.path.isfile(LOG_FILE_NAME)
    
    try:
        # Open the file in append mode. 'newline=""' is important to prevent blank rows.
        with open(LOG_FILE_NAME, 'a', newline='') as csvfile:
            # Define the column headers for the CSV file
            fieldnames = ['timestamp', 'cpu_percent', 'memory_percent']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # If the file is new, write the header row
            if not file_exists:
                writer.writeheader()
                print(f"Log file '{LOG_FILE_NAME}' created with headers.")
                
    except IOError as e:
        print(f"Error: Could not open or write to log file {LOG_FILE_NAME}. {e}")
        # Exit if we can't write to the log file
        exit(1)

def log_metrics(cpu_percent, memory_percent):
    """
    Appends the latest performance metrics to the CSV log file.
    
    Args:
        cpu_percent (float): The current CPU usage.
        memory_percent (float): The current memory usage.
    """
    try:
        with open(LOG_FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['timestamp', 'cpu_percent', 'memory_percent'])
            
            # Get the current timestamp in a readable format
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Write the data to the file
            writer.writerow({
                'timestamp': timestamp,
                'cpu_percent': cpu_percent,
                'memory_percent': memory_percent
            })
            
            # Also print to console for real-time monitoring
            print(f"{timestamp} - CPU: {cpu_percent}% | Memory: {memory_percent}%")
            
    except IOError as e:
        print(f"Error: Could not write to log file {LOG_FILE_NAME}. {e}")

def main():
    """
    Main function to run the monitoring loop.
    """
    print("--- System Performance Monitor ---")
    print(f"Logging CPU and memory usage every {LOG_INTERVAL_SECONDS} seconds.")
    print(f"Data will be saved to '{LOG_FILE_NAME}'.")
    print("Press Ctrl+C to stop the script.")
    
    # Ensure the log file is ready for writing
    setup_log_file()
    
    try:
        # Start the monitoring loop
        while True:
            # Get the metrics
            cpu, mem = get_performance_metrics()
            
            # Log them to the file
            log_metrics(cpu, mem)
            
            # Wait for the specified interval before the next reading
            time.sleep(LOG_INTERVAL_SECONDS)
            
    except KeyboardInterrupt:
        # Handle the user pressing Ctrl+C
        print("\nMonitoring stopped by user. Log file saved.")
    except Exception as e:
        # Handle other potential errors
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
