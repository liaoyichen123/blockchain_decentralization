import csv
import glob

# Define the pattern to match the CSV files you want to merge
# pattern = 'path/to/your/csv/files/*.csv'  # Adjust the path as needed
pattern = 'C:/Users/Ze/Downloads/blockchain_decentralization-main/blockchain_decentralization-main/cvs/*.csv'
# Use glob to list all files that match the pattern

csv_files = glob.glob(pattern)

# Open a new CSV file for writing the merged content
with open('merged_file.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    for file in csv_files:
        with open(file, 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                writer.writerow(row)