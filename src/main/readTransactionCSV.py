# import csv

# # Path to your CSV file
# csv_file_path = "bofatransactions.csv"

# # Lists to store transaction data
# dates = []
# transaction_names = []
# amounts = []
# running_balances = []

# # List to store skipped lines
# skipped_lines = []

# # Read CSV file, skipping problematic lines and collecting them
# try:
#     with open(csv_file_path, 'r') as file:
#         csv_reader = csv.reader(file, quotechar='"')
#         for line_number, line_content in enumerate(csv_reader):
#             # Skip empty lines
#             if not line_content:
#                 skipped_lines.append(line_content)
#                 continue
            
#             try:
#                 # Extract data from line_content
#                 date = line_content[0]
#                 transaction_name = line_content[1]
#                 amount = line_content[2]
#                 running_balance = line_content[3]
                
#                 # Append data to lists
#                 dates.append(date)
#                 transaction_names.append(transaction_name)
#                 amounts.append(amount)
#                 running_balances.append(running_balance)
#             except (IndexError, ValueError):
#                 skipped_lines.append(line_content)
# except FileNotFoundError:
#     print("File not found:", csv_file_path)

# # Display the skipped lines
# if skipped_lines:
#     print("Skipped lines:")
#     for line in skipped_lines:
#         print(line)

# # Display the lists containing transaction data
# print("Dates:", dates)
# print("Transaction Names:", transaction_names)
# print("Amounts:", amounts)
# print("Running Balances:", running_balances)

import csv

def read_csv_file(csv_file_path):
    """
    Reads a CSV file and returns the parsed lines.
    """
    parsed_lines = []
    skipped_lines = []

    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file, quotechar='"')
            for line_number, line_content in enumerate(csv_reader):
                if not line_content:
                    skipped_lines.append(line_content)
                else:
                    parsed_lines.append(line_content)
    except FileNotFoundError:
        print("File not found:", csv_file_path)

    return parsed_lines, skipped_lines

def parse_lines(parsed_lines):
    """
    Parses the lines and extracts transaction data.
    """
    transaction_data = {
        'dates': [],
        'transaction_names': [],
        'amounts': [],
        'running_balances': []
    }

    for line_content in parsed_lines:
        try:
            date = line_content[0]
            transaction_name = line_content[1]
            amount = line_content[2]
            running_balance = line_content[3]

            transaction_data['dates'].append(date)
            transaction_data['transaction_names'].append(transaction_name)
            transaction_data['amounts'].append(amount)
            transaction_data['running_balances'].append(running_balance)
        except (IndexError, ValueError):
            print("Error parsing line:", line_content)

    return transaction_data

def print_skipped_lines(skipped_lines):
    """
    Prints the skipped lines.
    """
    if skipped_lines:
        print("Skipped lines:")
        for line in skipped_lines:
            print(line)

def print_transaction_data(transaction_data):
    """
    Prints the transaction data.
    """
    for key, values in transaction_data.items():
        print(key.capitalize() + ":", values)

def search_amount_by_transaction_name(transaction_data, searched_transaction_name):
    """
    Searches for the amount corresponding to a transaction name.
    """
    for i, name in enumerate(transaction_data['transaction_names']):
        if name == searched_transaction_name:
            return transaction_data['amounts'][i]
    return None


# TESTING METHODS
# Path to your CSV file
csv_file_path = "bofatransactions.csv"

# Read the CSV file
parsed_lines, skipped_lines = read_csv_file(csv_file_path)

# Parse the lines and extract transaction data
transaction_data = parse_lines(parsed_lines)

# Print skipped lines
print_skipped_lines(skipped_lines)

# Print transaction data
print_transaction_data(transaction_data)

# Example: Search for transaction amount by transaction name
searched_transaction_name = ""
amount = search_amount_by_transaction_name(transaction_data, searched_transaction_name)
if amount is not None:
    print("Amount for transaction", searched_transaction_name, ":", amount)
else:
    print("Transaction name not found:", searched_transaction_name)
