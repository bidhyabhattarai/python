import os  # for device drives
import shutil  # files input and output

# path to organize - FIXED
path_to_organise = r"C:\Users\zenith\Desktop"  # Use raw string for Windows paths

# define all file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".wmv", ".mkv"],
    "Archives": [".zip", ".tar", ".tar.gz", ".tar.bz", ".rar", ".7z"],
    "Music": [".mp3", ".m4a", ".flac", ".wav"]
}

# loop through my path where i need to organise and list them
for filename in os.listdir(path_to_organise):
    print(filename)
    file_path = os.path.join(path_to_organise, filename)
    print(file_path)

    # skip folders/directories
    if os.path.isdir(file_path):
        continue

    # check for each file extension and then move to respective created folders
    moved = False
    for folder, extensions in file_types.items():
        if filename.lower().endswith(tuple(extensions)):
            folder_path = os.path.join(path_to_organise, folder)
            # if there is no folder then create
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # move the files to folder
            shutil.move(file_path, folder_path)
            moved = True
            print(f"Moved {filename} to {folder}/")
            break

    # FIXED: This should be outside the for loop
    if not moved:
        others_path = os.path.join(path_to_organise, "Others_Files")
        if not os.path.exists(others_path):
            os.makedirs(others_path)
        shutil.move(file_path, others_path)
        print(f"Moved {filename} to Others_Files/")

print("✓ All files moved successfully!")