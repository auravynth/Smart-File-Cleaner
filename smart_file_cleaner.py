import os
import re
import sys


def clean_filename(filename):
    """Return a cleaned version of a filename."""
    name, extension = os.path.splitext(filename)
    name = re.sub(r"[_\-]+", " ", name)
    name = re.sub(r"[^a-zA-Z0-9 ]+", "", name)
    name = " ".join(name.split())

    return filename if not name else f"{name}{extension}"


def get_unique_name(directory, filename):
    """Return a non-conflicting filename."""
    base, extension = os.path.splitext(filename)
    candidate = filename
    counter = 1

    while os.path.exists(os.path.join(directory, candidate)):
        candidate = f"{base} ({counter}){extension}"
        counter += 1

    return candidate


def clean_folder(directory):
    """Rename files in a directory using cleaned filenames."""
    renamed = 0

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        if not os.path.isfile(old_path):
            continue

        new_filename = clean_filename(filename)

        if new_filename == filename:
            continue

        new_path = os.path.join(directory, new_filename)

        if os.path.exists(new_path):
            new_filename = get_unique_name(directory, new_filename)
            new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f"[RENAMED] {filename} -> {new_filename}")
        renamed += 1

    return renamed


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    if not os.path.isdir(directory):
        print(f"Error: directory not found: {directory}")
        sys.exit(1)

    print(f"Cleaning filenames in: {os.path.abspath(directory)}")
    print("-" * 60)
    total = clean_folder(directory)
    print("-" * 60)
    print(f"Completed. {total} file(s) renamed.")


if __name__ == "__main__":
    main()
