import os
import shutil
import sys
import time

def custom_loader(sec:float):
    chars = ["-", "\\", "|", "/"]
    for _ in range(20):
        for char in chars:
            sys.stdout.write(f"\rFile Organization in Progress {char} ")
            sys.stdout.flush()
            time.sleep(sec)
    print("\nDone!")

print("Welcome to Python Automation Script for File Handling".center(150))


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"New directory '{directory}' has been created")

def main():
    path = input("Please enter the directory path for File Organization:\n")
    while True:
        filetype = input('''Enter the file type (e.g., "docx", "pdf", etc.) that you want to organize: \n''')
        subdirectory = os.path.join(path, filetype)
        if not os.path.exists(subdirectory):
            print(f"Error: Directory for '{filetype}' not found. Please enter a valid file type.")
        else:
            break

    custom_loader(0.05)

    # Organize files
    files = os.listdir(path)
    for file in files:
        root, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the leading dot
        oldpath = os.path.join(path, file)
        newpath = os.path.join(path, extension, file)
        try:
            shutil.move(oldpath, newpath)
            print(f"Moved '{file}' to '{newpath}'")
            print("Operation Successful!")
        except FileNotFoundError:
            print(f"Error: File '{file}' not found or destination directory missing.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
