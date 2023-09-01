import os
import shutil

def File_organizer_by_extension(directory_path):
    if not os.path.exists(directory_path):
        print("Directory does not exist.\n------------> Please Try Again !\n")
        return

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file in files:
        _, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot from the extension
        print(extension)
        if extension:
            # Create a subdirectory if it doesn't exist
            if not os.path.exists(os.path.join(directory_path, extension)):
                os.mkdir(os.path.join(directory_path, extension.capitalize()))

            # Move the file to the corresponding subdirectory
            src = os.path.join(directory_path, file)
            dest = os.path.join(directory_path, extension, file)

            shutil.move(src, dest)
            print(f"Moved {file} to {extension} directory.")


if __name__ == "__main__":

    print(""" ___                                  _     ____
|_ _|_ __  _ __   ___   ___ ___ _ __ | |_  | __ )  ___  _   _
 | || '_ \| '_ \ / _ \ / __/ _ \ '_ \| __| |  _ \ / _ \| | | |
 | || | | | | | | (_) | (_|  __/ | | | |_  | |_) | (_) | |_| |
|___|_| |_|_| |_|\___/ \___\___|_| |_|\__| |____/ \___/ \__, |
                                     Noting Impossible  |___/ """)
    while True:
        print("1. Organize File.\n2. Exit.")
        input_value=input("Enter Option: ")

        print()
        if input_value=='1':
            directory_path = input("Enter the directory path to organize Like-->[F:\]: ")
            print()
            retrun_file=File_organizer_by_extension(directory_path)
        else:
            break

