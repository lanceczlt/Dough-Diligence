import pandas as pd
import io

# Path to your CSV file
csv_file_path = "transactions.csv"

# List to store skipped lines
skipped_lines = []

# List to store regular lines
regular_lines = []

# Read CSV file, skipping problematic lines and collecting them
try:
    with open(csv_file_path, 'r') as file:
        for line_number, line_content in enumerate(file):
            # Skip empty lines
            if not line_content.strip():
                skipped_lines.append(line_content)
                continue
            
            try:
                pd.read_csv(io.StringIO(line_content))
                regular_lines.append(line_content)
            except pd.errors.ParserError:
                skipped_lines.append(line_content)
except FileNotFoundError:
    print("File not found:", csv_file_path)

# Display the regular lines
if regular_lines:
    print("Regular lines:")
    for line in regular_lines:
        print(line)

# Display the skipped lines
if skipped_lines:
    print("Skipped lines:")
    for line in skipped_lines:
        print(line)

# # Define the chunk size, i.e., how many rows to read at a time
# chunk_size = 1000

# data = pd.read_csv(csv_file_path, error_bad_lines=False)

# # Iterate over chunks of the CSV file
# for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
#     # Process each chunk
#     for index, row in chunk.iterrows():
#         # Access each row
#         print(row)
#         # Process the row as needed
