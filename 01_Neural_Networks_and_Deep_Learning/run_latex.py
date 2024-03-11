import os
import subprocess
import shutil


def move_file(file_name, folder_name):
    """Move file to a folder
    """
    # create a new directory
    os.makedirs(folder_name, exist_ok=True)
    # path of the file when moved
    destination_file = os.path.join(folder_name, os.path.basename(file_name))
    try:
        shutil.move(file_name, folder_name)
    except shutil.Error:
        os.remove(destination_file)
        shutil.move(file_name, folder_name)
    except FileNotFoundError:
        print("Please put the raw data file in the same directory as this python file")


def clean():
    temp_folder = '.LaTeXtemp'

    for file in os.listdir(os.getcwd()):
        if file.endswith('.aux') or file.endswith('.log'):
            move_file(file, temp_folder)


def execute():
    print("Running latex")
    file_name = None
    for file in os.listdir(os.getcwd()):
        if file.endswith(".tex"):
            file_name = file
            print(file_name)
    subprocess.run(["xelatex", f"{file_name}"])
    clean()


if __name__ == '__main__':
    execute()
