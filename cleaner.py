import psycopg2
import pandas as pd
import ast
from datetime import datetime

# Database connection parameters
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Deepika@04",
    "host": "localhost",
    "port": "5432"  # Default PostgreSQL port
}

# Load the CSV file
csv_file_path = "C:\\Users\\sridh\\OneDrive\\Documents\\data-1740630514569.csv"
df = pd.read_csv(csv_file_path)

# Remove duplicate rows based on link_id
df.drop_duplicates(subset=["link_id"], keep="first", inplace=True)

# Drop rows where link_id is NaN (since it is UNIQUE)
df = df.dropna(subset=["link_id"])

# Handle missing integer values
df["id"] = df["id"].fillna(-1).astype("int64")  # Assigning -1 to missing IDs
df["mid"] = df["mid"].fillna(-1).astype("int64")  # Assigning -1 to missing Merchant IDs

# Convert `created_on` to datetime and replace invalid values with a default timestamp
df["created_on"] = pd.to_datetime(df["created_on"], errors="coerce")
df["created_on"] = df["created_on"].fillna(datetime(1970, 1, 1))  # Default timestamp for missing values

# Convert vector_embedding from string to list format for pgvector
df["vector_embedding"] = df["vector_embedding"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

# Logging variables
inserted_count = 0
skipped_count = 0

# Insert data row by row with logging
for _, row in df.iterrows():
    try:
        query = """
        INSERT INTO udemy_courses_demo (
            id, mid, merchant_name, link_id, created_on, sku,
            product_name, category_primary, category_secondary,
            price, sale_price, description, link_url, image_url,
            full_text, vector_embedding
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(query, (
            row["id"], row["mid"], row["merchant_name"], row["link_id"],
            row["created_on"], row["sku"], row["product_name"], row["category_primary"],
            row["category_secondary"], row["price"], row["sale_price"], row["description"],
            row["link_url"], row["image_url"], row["full_text"], row["vector_embedding"]
        ))
        inserted_count += 1
        print(f"✅ Inserted: {row['product_name']} (link_id: {row['link_id']})")

    except psycopg2.errors.UniqueViolation:
        conn.rollback()  # Rollback the transaction for that row
        skipped_count += 1
        print(f"⚠️ Skipped (Duplicate link_id): {row['product_name']} (link_id: {row['link_id']})")
    
    except Exception as e:
        conn.rollback()  # Rollback the transaction for that row
        skipped_count += 1
        print(f"❌ Error inserting: {row['product_name']} (link_id: {row['link_id']}) | Error: {str(e)}")

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print(f"\nSummary: ✅ {inserted_count} records inserted, ⚠️ {skipped_count} records skipped.")