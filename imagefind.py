'''
#! python3
 imagefind.py - Finds image files in a user-inputted directory and copies them to a
  new folder in that directory.
'''

import os
import shutil


def main():
    '''
    Function creates directory to store new files in. Searches file tree for all files.
    Finds files with required extensions and copies them to new directory.
    '''
    # Create new directory for copied files.

    dir_name = input("Enter your directory: ")
    new_folder = input("Enter a name for your new folder: ")

    if not os.path.exists(os.path.join(dir_name, new_folder)):
        os.mkdir(os.path.join(dir_name, new_folder))
    # Set path of new dir.
    new_path = os.path.join(dir_name, new_folder)
    # Get list of files in provided dir, by walking through file tree.
    file_list = list()
    for (dirpath, _, filenames) in os.walk(dir_name):
        file_list += [os.path.join(dirpath, filename)
                      for filename in filenames]
    # For each filename check for required extension. Generate source path of file
    # and copy to new dir.
    for filename in file_list:
        if filename.lower().endswith(('.jpeg', '.pdf', '.png', '.gif')):
            sourcepath = os.path.abspath(filename)
            shutil.copy(sourcepath, new_path)


if __name__ == '__main__':
    main()
