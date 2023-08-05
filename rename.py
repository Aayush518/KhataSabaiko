import os
import time

folder_path = r'D:\accounting-with-vat\known_faces'  # Replace with the actual folder path
new_name = 'Aayush'  # Replace with the base name you want to use

# Iterate over all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust the file extensions as per your requirement
        # Get the full path of the file
        old_filepath = os.path.join(folder_path, filename)

        # Get the current timestamp as a unique identifier
        timestamp = str(int(time.time()))

        # Create the new filename with the base name, unique identifier, and the original file extension
        new_filename = new_name + '_' + timestamp + os.path.splitext(filename)[1]

        # Get the full path of the new file
        new_filepath = os.path.join(folder_path, new_filename)

        # Check if the new file name already exists and append a counter to make it unique
        counter = 1
        while os.path.exists(new_filepath):
            new_filename = new_name + '_' + timestamp + '_' + str(counter) + os.path.splitext(filename)[1]
            new_filepath = os.path.join(folder_path, new_filename)
            counter += 1

        # Rename the file
        os.rename(old_filepath, new_filepath)

print('File renaming completed!')
