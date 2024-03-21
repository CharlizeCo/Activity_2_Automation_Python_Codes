import os
import sys
from google.cloud import storage

def get_file_size(bucket_name, blob_name):
    try:
        # Initialize Google Cloud Storage client
        storage_client = storage.Client()

        # Get the bucket and blob
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Download the blob to a temporary file
        act2.txt = "/Users/rabbi/act2.txt"
        blob.download_to_filename(act2.txt)

        # Get the file size
        file_size = os.stat(act2.txt)

        # Delete the temporary file
        os.remove(act2.txt)

        return file_size

    except Exception as e:
        print("Error downloading file from GCP Storage.")
        sys.exit(1)

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Incorrect number of command-line arguments.")
        sys.exit(1)

    bucket_name = sys.argv[1]
    blob_name = sys.argv[2]

    file_size = get_file_size(bucket_name, blob_name)
     print("File size:", file_size, "bytes")

if __name__ == "__main__":
    main()
