import os
from datetime import datetime

# Get the directory containing the files
dir_path = input("Enter the path to the directory containing the files: ")

# Check if the directory exists
if not os.path.isdir(dir_path):
  print(f"Directory not found: {dir_path}")
  exit(1)

# Get the new filename from the user
new_filename = input("Enter the new filename: ")

# Validate the new filename
if not new_filename:
  print("No filename provided.")
  exit(1)

# Loop through all the files in the directory
for filename in os.listdir(dir_path):
  # Skip the file if its name is the same as the new filename
  if filename == new_filename:
    continue

  # Get the file's creation time
  creation_time = os.path.getctime(os.path.join(dir_path, filename))

  # Convert the creation time to a readable format
  creation_time_str = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d_%H-%M-%S")

  # Construct the new file name
  new_file_name = f"{new_filename}_{creation_time_str}{os.path.splitext(filename)[1]}"

  # Rename the file
  os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_file_name))
