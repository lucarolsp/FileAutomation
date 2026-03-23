# FileAutomation

## 
Downloads Folder Organizer is a lightweight Python script that automatically sorts files in your Downloads folder into clearly named subfolders based on file type. 

## Features

•	Organizes files into categories: PDFs, Images, Music, Videos, Compressed, Documents

•	Unrecognized file types are moved to an Others folder

•	Skips subfolders — only processes files

•	Prints a summary report after each run

•	Zero external dependencies — pure Python standard library


## Installation

• Clone or download this repository

• Navigate into the project folder:
cd downloads-organizer


## Run with automatic path 

By default, the script targets the current user's Downloads folder:
python organizer.py

## Run with a custom path

Open the script and uncomment the manual path option at the bottom of the file:
    manual_downloads = pathlib.Path('/Users/YourName/Downloads')
    organize_folder(manual_downloads)


## File Categories

Folder	.Extensions

PDFs	.pdf

Images	.jpg  .jpeg  .png  .gif  .bmp  .webp  .svg

Music	.mp3  .wav  .flac  .aac  .ogg

Videos	.mp4  .mov  .avi  .mkv  .wmv

Compressed	.zip  .rar  .7z  .tar  .gz

Documents	.docx  .xlsx  .pptx  .txt  .csv

Others	Everything else


## Example Output
  
  Organizing: /Users/john/Downloads

  report_2024.pdf          →  PDFs/
  
  holiday_photo.jpg        →  Images/
  
  favourite_song.mp3       →  Music/
  
  project_backup.zip       →  Compressed/
  
  meeting_notes.docx       →  Documents/
  
  unknown_file.xyz         →  Others/


## Project Structure

downloads-organizer/

├── organizer.py     
└── README.md        




