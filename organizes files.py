import os
import shutil

def organize_files(directory):
    # Step 1: Create a folder to store the organized files
    organized_folder = os.path.join(directory, "organized_files")
    if not os.path.exists(organized_folder):
        os.mkdir(organized_folder)

    # Step 2: Get a list of all files in the directory
    all_files = os.listdir(directory)

    # Step 3: Organize files by extension
    for file in all_files:
        # Check if the item in the directory is a file (not a folder)
        if os.path.isfile(os.path.join(directory, file)):
            # Step 4: Get the file extension without the dot
            file_extension = os.path.splitext(file)[1][1:]

            # Step 5: Create a subdirectory for each unique extension if it doesn't exist
            subdirectory = os.path.join(organized_folder, file_extension)
            if not os.path.exists(subdirectory):
                os.mkdir(subdirectory)

            # Step 6: Move the file to the corresponding subdirectory
            source_file = os.path.join(directory, file)
            destination_file = os.path.join(subdirectory, file)
            shutil.move(source_file, destination_file)

if __name__ == "__main__":
    # Step 7: Specify the directory to organize files (change this path to your desired directory)
    target_directory = "D:\organized_files"

    # Step 8: Call the function to organize files in the directory
    organize_files(target_directory)
