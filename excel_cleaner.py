import pandas as pd

def preprocess_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Display the first few rows of the original data
    print("Original Data:")
    print(df.head())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values (e.g., fill with mean or drop)
    df.fillna(method='ffill', inplace=True)  # Forward fill for missing values

    # Rename columns if necessary
    df.rename(columns={'OldColumnName': 'NewColumnName'}, inplace=True)

    # Display the first few rows of the cleaned data
    print("Cleaned Data:")
    print(df.head())

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False, quoting=1)  # quoting=1 ensures proper quotes

if __name__ == "__main__":
    input_file = "C:\\Users\\sridh\\Downloads\\imported_data.csv"  # Specify the path to your input CSV file
    output_file = "C:\\Users\\sridh\\Downloads\\cleaned_data.csv"  # Specify the path for the output cleaned CSV file
    preprocess_csv(input_file, output_file)
