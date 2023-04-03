import csv
import re
import sys

# Get the CSV filename from the command line arguments
if len(sys.argv) < 2:
    print("Please provide the CSV filename as a command line argument.")
    sys.exit()
csv_filename = sys.argv[1]

# Extract the integer number from the CSV filename using regular expressions
match = re.search(r'\d+', csv_filename)
if match:
    num = match.group()
else:
    num = '0'

# Open the CSV file for reading
with open(csv_filename, 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Create a list of binary values from the hexadecimal values
    binary_data = []
    for row in reader:
        hex_string = ''.join(row)  # Combine all hex values in the row into a single string
        for i in range(0, len(hex_string), 32):
            hex_value = hex_string[i:i+32]  # Extract a 32-character substring of hex values
            binary_data.append(bytes.fromhex(hex_value))

# Write the binary data to a new file with the format "number_key_binary.bin"
binary_filename = f"{num}_key_binary.bin"
try:
    with open(binary_filename, 'wb') as binary_file:
        for binary_value in binary_data:
            binary_file.write(binary_value)
finally:
    # Close the file object explicitly in case of any exceptions
    binary_file.close()
