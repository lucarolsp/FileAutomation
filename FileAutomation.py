# File Organizer for the Downloads Folder
# This script organizes files in the Downloads folder


# Library imports

import os       # for navigating folders and checking files
import shutil   # for moving and copying files
import pathlib  # modern way of working with file paths


# Here you define which extensions go into which folder.
# A "dictionary" in Python works like a table: key → value

FILE_TYPES = {
    "PDFs":      [".pdf"],
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Music":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos":    [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Compressed":[".zip", ".rar", ".7z", ".tar", ".gz"],
    "Documents": [".docx", ".xlsx", ".pptx", ".txt", ".csv"],
}

# Folder for files that don't fit into any category
OTHER_FOLDER = "Others"


# Main function that organizes files in the specified folder
def organize_folder(downloads_path):
    folder = pathlib.Path(downloads_path) # Converts the path string into a Path object (easier to work with)
    if not folder.exists(): # Check if the folder exists before continuing
        print(f"Folder not found: {folder}")
        return  # 'return' with no value = exit the function

    print(f"\nOrganizing: {folder}")
    print("─" * 50)

    # Counters for the final report
    moved = 0
    skipped = 0

    # 'for' iterates over each item inside the folder
    for file in folder.iterdir():
        if file.is_dir(): # Skip subfolders (we only want files)
            skipped += 1
            continue  # 'continue' = jump to the next iteration

        # Get the file extension (e.g. ".pdf", ".jpg")
        # .lower() converts to lowercase: ".PDF" → ".pdf"
        extension = file.suffix.lower()
        destination_folder_name = find_category(extension) # Determine which folder this file should go into
        destination_folder = folder / destination_folder_name  # Build the full path of the destination folder
        # the "/" operator joins paths in pathlib
        destination_folder.mkdir(exist_ok=True) # Create the destination folder if it doesn't exist yet
        # exist_ok=True → no error if the folder already exists
        final_destination = destination_folder / file.name
        shutil.move(str(file), str(final_destination))

        print(f"  {file.name}  →  {destination_folder_name}/")
        moved += 1

    print("─" * 50)
    print(f"Done! {moved} files organized, {skipped} folders skipped.\n")


def find_category(extension):

    # Iterate over the FILE_TYPES dictionary
    # 'folder' = key (folder name), 'extensions' = value (list of extensions)
    for folder, extensions in FILE_TYPES.items():

        # Check if the extension is in this category's list
        if extension in extensions:
            return folder  # found it! return the folder name

    # If the 'for' loop finished without finding anything, fall back to "Others"
    return OTHER_FOLDER


# ENTRY POINT
# This block only runs when you execute the file directly
# (not when it's imported by another script)

if __name__ == "__main__":

    # ── OPTION 1: Automatic path (user's Downloads folder) ──
    automatic_downloads = pathlib.Path.home() / "Downloads"

    # ── OPTION 2: Manual path (uncomment and edit if you prefer) ──
    # manual_downloads = pathlib.Path("/Users/YourName/Downloads")

    # Run the organizer
    organize_folder(automatic_downloads)