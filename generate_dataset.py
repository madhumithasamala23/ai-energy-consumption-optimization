import pandas as pd
import random

data = []

for _ in range(250):
    temperature = random.randint(18, 40)
    humidity = random.randint(30, 85)
    occupancy = random.randint(10, 300)
    hour = random.randint(0, 23)
    is_weekend = random.choice([0, 1])

    # Simulated energy consumption logic
    energy_consumption = (
        temperature * 2 +
        humidity * 1.5 +
        occupancy * 1.2 +
        (50 if hour >= 18 else 20) +
        (30 if is_weekend else 0)
    )

    data.append([
        temperature,
        humidity,
        occupancy,
        hour,
        is_weekend,
        round(energy_consumption, 2)
    ])

df = pd.DataFrame(data, columns=[
    "temperature",
    "humidity",
    "occupancy",
    "hour",
    "is_weekend",
    "energy_consumption"
])

df.to_csv("data/energy_data.csv", index=False)

print("✅ Dataset with 250 rows created successfully")
