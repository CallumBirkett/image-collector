#! python3
# imagefind.py - Finds image files in a user-inputted directory and copies them to a
#  new folder in that directory.

# TODO: Turn this into a function. Q: Do we need a main() statement?

import os
import shutil
import sys

#  Write a user input to detect directory path.

user_input = input("Enter your directory: ")
user_input_1 = input("Enter a name for your new folder: ")

# Create new folder based on user input.
if not os.path.exists(os.path.join(user_input, user_input_1)):
    os.mkdir(os.path.join(user_input, user_input_1))
# else:
#     print("The folder you are trying to create already exists.")

# Create variable to call new folder.
new_dir = os.path.join(user_input, user_input_1)

# TODO: We want to search through all subfolders as well.

# Check if filename ends in a image extention. If it does, copy it to new folder.
for filename in os.listdir(user_input):
    if filename.endswith(('.jpeg', '.pdf', '.png', '.gif')):
        loc = os.path.abspath(filename)
        dest = os.path.join(new_dir, filename)
        print('\nImage file found at: ' + loc + '\n')
        print('Moving image to: ' + dest + '\n')
        shutil.copy(loc, dest)
