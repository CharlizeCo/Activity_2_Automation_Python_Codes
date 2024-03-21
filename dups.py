import os
import hashlib
import sys

def find_duplicate_files(directory):
    checksums = {}
    duplicates = []

    # Iterate through all files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                # Calculate MD5 checksum for each file
                with open(filepath, 'rb') as f:
                    file_content = f.read()
                    checksum = hashlib.md5(file_content).hexdigest()

                    # Add file to dictionary using checksum as key
                    if checksum in checksums:
                        checksums[checksum].append(filepath)
                    else:
                        checksums[checksum] = [filepath]

    # Identify duplicates
    for checksum, files in checksums.items():
        if len(files) > 1:
            duplicates.append((checksum, files))

    return duplicates

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python dups.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    
    # Check if the specified directory exists
    if not os.path.isdir(directory):
        print("Error: Directory not found.")
        sys.exit(1)

    # Find duplicate files
    duplicates = find_duplicate_files(directory)

    # Output duplicate files and their checksums
    if duplicates:
        print("Duplicate files found:")
        for checksum, files in duplicates:
            print("Checksum:", checksum)
            for file in files:
                print("-", file)
            print()
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
