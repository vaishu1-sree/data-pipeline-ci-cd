import pandas as pd
import numpy as np
import os

os.makedirs("input_data", exist_ok=True)

for i in range(10):
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='T'),
        'temperature': np.random.normal(25, 2, 100),
        'humidity': np.random.normal(60, 5, 100),
        'pressure': np.random.normal(1013, 10, 100)
    })

    if i % 3 == 0:  # Add corrupt data to some files
        df.loc[10:15, 'temperature'] = np.nan

    df.to_csv(f'input_data/sensor_data_{i}.csv', index=False)

print("✅ Synthetic sensor data created.")
