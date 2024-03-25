# Serial_Plotter
The code establishes communication with the microcontroller, continuously reads data from it, updates a plot to visualize the received data, and maintains this visualization in real-time. It provides a flexible and dynamic way to monitor and analyze data streaming from a microcontroller over a serial connection.


To ensure that the information arriving through the serial port is correctly read by the provided code, it must follow a specific format. In this case, the information should have the following format:

  SignalName0=Value/SignalName1=Value/SignalName2=Value..."

Each signal is represented by a name (e.g., "Signal0", "Signal1", etc.). After the signal name, there is an equal sign "=" that separates the name from the associated value. The value of the signal follows the equal sign and is a numerical representation of the transmitted data. After each name-value pair, there is a forward slash "/" that separates each signal-value pair. For example, a valid set of data that could be correctly read by the code would be something like:

  Signal0=10/Signal1=20/Signal2=15/Signal3=30/...

Where each signal has an associated value and they are separated by forward slashes ("/") as described above. If the incoming information does not follow this exact format, the code may not be able to interpret it correctly and could result in reading or parsing errors.
