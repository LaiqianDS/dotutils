import os
import shutil


def organize_folder(folder):
    file_types = {
        "Images": [".jpeg", ".jpg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Archives": [".zip", ".rar"],
    }
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()

                for folder_name, extensions in file_types.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder, folder_name)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_folder, filename))
                        print(f"Moved {filename} to {folder_name}")
                        break
    except FileNotFoundError:
        print("The specified folder does not exist")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)

    return


if __name__ == "__main__":
    target_directory = input("Enter the path of the folder to organize: ")
    organize_folder(target_directory)
