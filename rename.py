import os
import re

def rename_gopro_videos(directory, base_name):
    # Regular expression for filenames like GH070829.MP4
    gopro_pattern = re.compile(r'^GH(\d{2})(\d{4})\.MP4$', re.IGNORECASE)
    
    # Dictionary to track segment numbers
    file_segments = {}

    # Traverse the directory for GoPro video files
    for filename in os.listdir(directory):
        match = gopro_pattern.match(filename)
        if match:
            segment_number = match.group(1)  # e.g., 07
            sequence_number = match.group(2)  # e.g., 0829
            extension = 'mp4'

            # Construct the new name
            new_name = f"{base_name}{sequence_number}-{segment_number}.{extension}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed {old_file} to {new_file}")

# Adjust the directory path to point to the SD card in drive X
directory = "/mnt/x/DCIM/100GOPRO"
base_name = "TB140924_"

rename_gopro_videos(directory, base_name)
