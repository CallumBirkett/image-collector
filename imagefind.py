#! python3
# imagefind.py - Finds image files in a user-inputted directory and copies them to a
#  new folder in that directory.

# TODO: Create tests.

import os
import shutil
import sys


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        path = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(path):
            allFiles = allFiles + getListOfFiles(path)
        else:
            allFiles.append(path)

    return allFiles


def main():

    if not os.path.exists(os.path.join(dirName, user_input)):
        os.mkdir(os.path.join(dirName, user_input))

    listOfFileNames = getListOfFiles(dirName)

    newPath = os.path.join(dirName, user_input)
    for filename in listOfFileNames:
        if filename.endswith(('.jpeg', '.pdf', '.png', '.gif')):
            sourcepath = os.path.abspath(filename)
            dest = os.path.join(newPath, filename)
            shutil.copy(sourcepath, dest)


dirName = input("Enter your directory: ")
user_input = input("Enter a name for your new folder: ")

if __name__ == '__main__':
    main()
