import fastf1
import pandas as pd
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache')

# Load race session
session = fastf1.get_session(2023, 'Monza', 'R')
session.load()

# Get all laps from all drivers
laps = session.laps

# Optional: Print unique drivers
print("Drivers in session:", laps['Driver'].unique())

# Save all laps to CSV
laps.to_csv('src/all_drivers_monza_2023.csv', index=False)

print("✅ Saved full race data to CSV.")
