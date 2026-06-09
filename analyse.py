import pandas as pd
df = pd.read_csv("sensor_log.csv")
anomalies = df[df['Voltage'] < 10.0]

print(df)
