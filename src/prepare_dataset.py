import pandas as pd

# Load lap data
laps = pd.read_csv('src/all_drivers_monza_2023.csv')

# Show what columns are available (debug)
print("📦 Columns in data:", list(laps.columns))

# Pick relevant columns (available in your dataset)
features = laps[['Driver', 'LapNumber', 'Compound', 'TyreLife', 'LapTime']].copy()

# Convert LapTime to seconds
features['LapTime'] = pd.to_timedelta(features['LapTime']).dt.total_seconds()

# Create a binary column: did this lap end in a pit?
# We check if TyreLife resets to 1 on the next lap — a simple trick
features['NextTyreLife'] = features.groupby('Driver')['TyreLife'].shift(-1)
features['PitNextLap'] = (features['NextTyreLife'] < features['TyreLife']).astype(int)

# Drop helper column
features.drop(columns=['NextTyreLife'], inplace=True)

# Drop rows with missing LapTime or TyreLife
features.dropna(inplace=True)

# Save to file
features.to_csv('src/ml_dataset_monza_2023.csv', index=False)

print("✅ ML dataset created successfully!")
