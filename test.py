import os
import re
import json
# Define the folders and prompt
source_folder = 'source'
target_folder = 'target'
prompt = "a mug"

# Collect all files from the source and target directories
source_files = os.listdir(source_folder)
target_files = os.listdir(target_folder)

# Function to extract the numeric index from the filename
def extract_index(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else None

# Sort the target files based on the numeric index
target_files_sorted = sorted(target_files, key=extract_index)

# Initialize an empty list to store the JSON data
json_lines = []

# Iterate over sorted target files and create the JSON objects
for target_file in target_files_sorted:
    # Extract the index from the target file name
    index = extract_index(target_file)

    # Find the corresponding source files based on the index
    source_files_for_index = [f for f in source_files if f.startswith(f'edge_image_{index}_')]

    # Generate JSON objects for each corresponding source file
    for source_file in source_files_for_index:
        json_entry = {"source": f"{source_folder}/{source_file}", "target": f"{target_folder}/{target_file}", "prompt": prompt}
        # Convert the JSON entry to a string
        json_line = json.dumps(json_entry)
        json_lines.append(json_line)

# Save each JSON line to a file or print the output
output_file = 'prompts.txt'
with open(output_file, 'w') as file:
    for line in json_lines:
        file.write(f"{line}\n")

print(f"JSON data written to {output_file}")
