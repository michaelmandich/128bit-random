import os
import sys

# Get the value of X from the command line arguments
if len(sys.argv) < 2:
    print("Please provide the value of X as a command line argument.")
    sys.exit()
x = sys.argv[1]

# Call the console command "./jawn X"
os.system(f"./jawn {x}")

# Call the Python script "converter.py" with the input file "Coutput_X_unique_values.csv"
os.system(f"Python3.6 converter.py Coutput_{x}_unique_values.csv")
