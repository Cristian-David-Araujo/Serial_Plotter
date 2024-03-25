# Serial_Plotter
The Serial Plotter is a Python script that establishes communication with a microcontroller, continuously reads data from it, updates a plot to visualize the received data, and maintains this visualization in real-time. It provides a flexible and dynamic way to monitor and analyze data streaming from a microcontroller over a serial connection.

## Installation
To use the Serial Plotter, you need to install the required libraries. You can install them using pip, the Python package manager. Run the following command:
```
pip install pyserial matplotlib
```

## Data Format
To ensure the correct interpretation of data received through the serial port, it must adhere to a specific format. The data should be structured as follows:
```
SignalName0=Value/SignalName1=Value/SignalName2=Value...
```
* Each signal is identified by a name (e.g., "Signal0", "Signal1", etc.).
* After the signal name, there is an equal sign "=" that separates the name from the associated value.
* The value of the signal follows the equal sign and is a numerical representation of the transmitted data.
* Each signal-value pair is separated by a forward slash "/".

For example, a valid set of data that can be correctly interpreted by the code would be:
```
Signal0=10/Signal1=20/Signal2=15/Signal3=30/...
```
If the incoming data does not adhere to this format, the code may encounter difficulties in interpreting it correctly, potentially resulting in reading or parsing errors. Therefore, it's crucial to ensure that the data follows the specified format for accurate processing by the Serial Plotter script.
