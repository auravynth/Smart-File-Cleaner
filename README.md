# Smart File Cleaner

A lightweight Python utility for cleaning and standardizing filenames in a directory.

## Features

- Replace underscores and hyphens with spaces
- Remove unnecessary special characters
- Normalize repeated spaces
- Preserve file extensions
- Prevent accidental overwrites
- Process the current directory or a selected directory
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer
- No third-party packages

## Usage

Run in the current directory:

    python smart_file_cleaner.py

Or provide a specific directory:

    python smart_file_cleaner.py "C:\Users\YourName\Downloads"

## Example

Before:

    My__Song--2026!!.mp3
    Project___Final---Version.pdf
    holiday___photos!!.jpg

After:

    My Song 2026.mp3
    Project Final Version.pdf
    holiday photos.jpg

## Safety

The script only renames files. It does not delete files, modify file contents, upload files, or install software.

For important files, test it on a copy of the directory first.

## License

MIT License.
