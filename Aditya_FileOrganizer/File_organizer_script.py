import os
import shutil

# Step 1: Define file types and categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".py", ".exe", ".js", ".java", ".cpp"]
}

# Step 2: Create folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Step 3: Organize files based on type
def organize_files(source_folder):
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                target_folder = os.path.join(source_folder, folder)
                create_folder(target_folder)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"Moved {file_name} to {folder}")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(source_folder, "Others")
            create_folder(others_folder)
            shutil.move(file_path, os.path.join(others_folder, file_name))
            print(f"Moved {file_name} to Others")
            
# Step 4: Run with predefined location
if __name__ == "__main__":
    path = input("Enter the path of the folder to organize: ").strip('"')
    if os.path.exists(path):
        organize_files(path)
        print("✅ Done organizing your files.")
    else:
        print("❌ Invalid path.")
