#! python3
# imagefind.py - Finds image files in a user-inputted directory and copies them to a
#  new folder in that directory.

import os
import shutil
import sys


def main():
    # Create new directory for copied files.
    if not os.path.exists(os.path.join(dirName, newFolder)):
        os.mkdir(os.path.join(dirName, newFolder))
    # Set path of new dir.
    newPath = os.path.join(dirName, newFolder)
    # Get list of files in provided dir, by walking through file tree.
    fileList = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        fileList += [os.path.join(dirpath, filename) for filename in filenames]
    # For each filename check for required extension. Generate source path of file
    # and copy to new dir.
    for filename in fileList:
        if filename.lower().endswith(('.jpeg', '.pdf', '.png', '.gif')):
            sourcepath = os.path.abspath(filename)
            shutil.copy(sourcepath, newPath)


dirName = input("Enter your directory: ")
newFolder = input("Enter a name for your new folder: ")

if __name__ == '__main__':
    main()
