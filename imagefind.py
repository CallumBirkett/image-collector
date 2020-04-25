#! python3
# imagefind.py - Finds image files in a user-inputted directory and copies them to a
#  new folder in that directory.

# TODO: Create tests.

import os
import shutil
import sys


def getListOfFiles(dirName):
    # Get list of objects in diretory.
    listDir = os.listdir(dirName)
    allFiles = list()
    # For each object, get type. If object = dir, repeat function.
    for entry in listDir:
        # Get the path of each object.
        path = os.path.join(dirName, entry)
        if os.path.isdir(path):
            allFiles = allFiles + getListOfFiles(path)
        else:
            allFiles.append(path)

    return allFiles


def main():
    # Create new directory for copied files.
    if not os.path.exists(os.path.join(dirName, newFolder)):
        os.mkdir(os.path.join(dirName, newFolder))
    # Set path of new dir.
    newPath = os.path.join(dirName, newFolder)
    # Get a list of filenames in the given dir.
    listOfFileNames = getListOfFiles(dirName)
    # For each filename check for required extension. Generate source path of file
    # and copy to new dir.
    for filename in listOfFileNames:
        if filename.lower().endswith(('.jpeg', '.pdf', '.png', '.gif')):
            sourcepath = os.path.abspath(filename)
            shutil.copy(sourcepath, newPath)


dirName = input("Enter your directory: ")
newFolder = input("Enter a name for your new folder: ")

if __name__ == '__main__':
    main()
