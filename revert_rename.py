import os
import re

def revert_gopro_filenames(directory):
    # Regular expression to match the renamed GoPro filenames 
    # !!! Change corresponding base name in RegEx
    gopro_pattern = re.compile(r'^TB240803_(\d{6})-(\d+)\.mp4$', re.IGNORECASE)

    for filename in os.listdir(directory):
        match = gopro_pattern.match(filename)
        if match:
            sequence_number = match.group(1)
            # Reconstruct the original filename
            original_name = f"GH{sequence_number}.MP4"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, original_name)
            
            # Rename the file back to the original name
            if os.path.exists(old_file):
                os.rename(old_file, new_file)
                print(f"Renamed {old_file} back to {new_file}")
            else:
                print(f"File {old_file} does not exist.")

# Adjust the directory path to where the files are located
directory = "/mnt/x/DCIM/100GOPRO"

revert_gopro_filenames(directory)
