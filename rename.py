import os

# Folder containing the images
folder_path = r"C:\Users\Admin\Documents\GitHub\pdd\Dataset2\data_split\validation\unhealthy"

# List all files in the directory and sort them
files = sorted(os.listdir(folder_path))

# Set starting index
start_index = 5329

# Loop through the files and rename them
for index, filename in enumerate(files, start=start_index):
    # Get the file extension
    file_ext = os.path.splitext(filename)[1]
    
    # New file name (healthy_5432, healthy_5433, ...)
    new_name = f"unhealthy_{index}{file_ext}"
    
    # Full old and new file paths
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)

print("Renaming complete!")
