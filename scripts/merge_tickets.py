import os
import pandas as pd

# --------------------------
# CONFIGURATION
# --------------------------
RAW_DATA_DIR = "data/raw"        # Folder containing multiple raw CSVs
MERGED_OUTPUT_PATH = "data/merged_tickets.csv"

# --------------------------
# 1. LOAD & MERGE ALL CSV FILES
# --------------------------
def merge_raw_tickets(input_dir, output_path):
    # Create output folder if missing
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Find all CSV files in the raw data folder
    csv_files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {input_dir}!")

    print(f"🔄 Found {len(csv_files)} raw CSV files. Starting merge...\n")

    df_list = []
    for file in csv_files:
        file_path = os.path.join(input_dir, file)
        try:
            df = pd.read_csv(file_path, encoding="latin1", low_memory=False)
            df["source_file"] = file  # Track which team/file this came from
            df_list.append(df)
            print(f"✅ Loaded: {file} | Shape: {df.shape}")
        except Exception as e:
            print(f"⚠️ Skipping {file} due to read error: {e}")

    # Concatenate all files into one DataFrame
    merged_df = pd.concat(df_list, ignore_index=True)

    print("\n📊 Before deduplication:", merged_df.shape)
    merged_df.drop_duplicates(inplace=True)
    print("📊 After deduplication:", merged_df.shape)

    # Save merged dataset
    merged_df.to_csv(output_path, index=False)
    print(f"🎉 Merged dataset saved to: {output_path} | Final shape: {merged_df.shape}")

    return merged_df

# --------------------------
# RUN SCRIPT
# --------------------------
if __name__ == "__main__":
    merged_df = merge_raw_tickets(RAW_DATA_DIR, MERGED_OUTPUT_PATH)
