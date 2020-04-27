'''
#! python3
imagefind.py - Finds files in a user-specified directory with given extentsions
and copies them to a new folder in that directory. Renames files, replacing
user-specified string with a replacement string.

Use Case: Copy image files from a set of subfolders into a new folder, replacing '.'
    with '_'.
Further: Script can be generalised by requiring that the user input their own choice
    of file extensions. A library could be constructed of those file extensions and
    fed to endswith().
 imagefind.py - Finds image files in a user-inputted directory and copies them to a
  new folder in that directory.
'''

import os
import shutil


def main():
    '''
    Function creates directory to store new files in. Searches file tree for all files.
    Finds files with required extensions and copies them to new directory, renaming
    them if necessary.
    '''
    # Ask for user inputs.
    dir_name = input("Enter your directory: ")
    new_folder = input("Enter a name for your new folder: ")
    key_string = input("Select a string you'd like to replace in filenames: ")
    replacement = input("Select a string you'd like to replace it with: ")
    # Set path of new dir.
    new_path = os.path.join(dir_name, new_folder)
    # Create new directory for copied files.
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    # Get list of files in provided dir, by walking through file tree.
    file_list = list()
    for (dirpath, _, filenames) in os.walk(dir_name):
        file_list += [os.path.join(dirpath, filename)
                      for filename in filenames]
    # For each filename check for required extension.
    # Generate source path of file and copy to new dir.
    for filename in file_list:
        if filename.lower().endswith(('.jpeg', '.pdf', '.png', '.gif')):
            sourcepath = os.path.abspath(filename)
            shutil.copy(sourcepath, new_path)
    # For each file in the new folder, rename it by given specification.
    for filename in os.listdir(new_path):
        # Split filename from extension and replace characters in filename.
        replace_filename = str(os.path.splitext(filename)[0]).replace(
            f'{key_string}', f'{replacement}')
        # Create a new filename from the replacement filename and old ext.
        new_filename = replace_filename + str(os.path.splitext(filename)[1])
        # Rename file.
        os.rename(os.path.join(new_path, filename),
                  os.path.join(new_path, new_filename))


if __name__ == '__main__':
    main()
