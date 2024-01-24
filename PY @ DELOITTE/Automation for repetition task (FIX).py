import os

def rename_files(directory_path, prefix):
    try:
        # Change to the specified directory
        os.chdir(directory_path)

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            if os.path.isfile(filename):  # Check if it's a file
                # Create a new filename with the specified prefix
                new_filename = f"{prefix}_{filename}"

                # Rename the file
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} to {new_filename}")

        print("Task completed successfully!")

    except FileNotFoundError:
        print(f"Error: Directory not found - {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = "/path/to/your/directory"
prefix = "new"
rename_files(directory_path, prefix)
