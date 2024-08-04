# rename-gopro-files

This script automates the naming of GoPro videos in a user-friendly way so that they are displayed in chronological order when sorted by name.

**Example Conversion:**

For the original file `GH070829.MP4:`
1. Segment Number: 07
2. Sequence Number: 0829
3. The script will rename it to: `{base_name}0829-07.mp4`

## Functionality:

1. **Search directory:** The script searches the specified directory for GoPro files.
2. **Recognise file names:** It uses a regular expression to recognise GoPro file names.
3. **Manage segment numbers:** It keeps a dictionary `(file_segments)` to manage the segment numbers for each sequence number.
4. **Rename files:** It creates a new file name in the format `GoPro{sequence_number}-{segment_number}.{extension}` and renames the files accordingly.

## Setup:

- **Customise directory:** Change the variable `directory` to specify the path to your directory with the GoPro video files. 
- **Adjust base name:** Change the variable `base_name` to specify the desired base name (e.g. GoPro) for the new file names.