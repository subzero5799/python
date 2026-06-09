import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sensor_log.csv")
anomalies = df[df['Voltage'] < 10.0]

print ("Raw Sensor Data")
print(df)

print("Anomalies Detected")
if anomalies.empty:
    print("System Stable, no anomalies found")
else:
    print(anomalies)

plt.figure(figure=(8,5))
plt.plot(df['Timestamp'], df['Voltage'], label = 'System Voltage', marker='o')

if not anomalies.empty: 
    plt.scatter(anomalies['Timestamp'], anomalies['Voltage'], color = 'red', s=150, label ='volage sag alert', zorder = 5)

plt.title('Hardware Telemetry: Voltage Degradation Alert')
plt.xlabel('Timestamp (Seconds)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)

plt.show()