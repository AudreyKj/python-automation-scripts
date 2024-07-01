import os
import shutil

def organize_screenshots(desktop_path, screenshots_folder):
    desktop_files = os.listdir(desktop_path)

    screenshots_path = os.path.join(desktop_path, screenshots_folder)
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path)

    for file_name in desktop_files:
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg') or file_name.lower().startswith('Screen Shot')):
            file_path = os.path.join(desktop_path, file_name)
            dest_path = os.path.join(screenshots_path, file_name)

            shutil.move(file_path, dest_path)
            print(f"Moved {file_name} ✨")

if __name__ == "__main__":
    desktop_path = "../Desktop" 
    screenshots_folder = "Screenshots"

organize_screenshots(desktop_path, screenshots_folder)
