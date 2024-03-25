import serial
import re
import matplotlib.pyplot as plt
from collections import deque
from time import time

# Serial port configuration
serial_port = '/dev/ttyUSB0'  # Change to the correct serial port
baud_rate = 9600  # Set the baud rate, ensure it matches the device

# Plot configuration
data_retention_time = 4  # Data retention time in seconds
samples_to_display = 100  # Number of samples to display on the plot

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Value')
ax.set_title('Serial Port Data')
plt.grid(True)

# Initialize data
initial_time = time()
data = {}
for i in range(10):
    data[f'Signal{i}'] = deque(maxlen=samples_to_display)

# Function to update the plot
def update_plot():
    ax.clear()
    for name, values in data.items():
        ax.plot(values, label=name)
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Value')
    ax.set_title('Serial Port Data')
    plt.grid(True)
    plt.pause(0.01)

# Main loop
while True:
    # Read line from the serial port
    line = ser.readline().decode().strip()
    
    # Parse the line for valid patterns
    matches = re.findall(r'(\w+)=(\d+)', line)
    if matches:
        # Update the data
        for name, value in matches:
            data[name].append(float(value))
        
        # Check if the retention time has passed
        current_time = time()
        if current_time - initial_time > data_retention_time:
            initial_time = current_time
            update_plot()

# Close the serial connection when exiting
ser.close()
