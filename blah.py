import pandas as pd

# Load the CSV file
file_path =r"C:\Users\sridh\OneDrive\Documents\cleaned_data.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Check if 'mid' column has non-integer values
df['mid'] = pd.to_numeric(df['mid'], errors='coerce')  # Convert to numeric, replace invalid values with NaN
df.dropna(subset=['mid'], inplace=True)  # Remove rows where 'mid' is NaN
df['mid'] = df['mid'].astype(int)  # Convert back to integer

# Save the cleaned file
cleaned_file_path = r"C:\Users\sridh\OneDrive\Documents\cleaned_data2.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"✅ Fixed CSV saved to {cleaned_file_path}")
