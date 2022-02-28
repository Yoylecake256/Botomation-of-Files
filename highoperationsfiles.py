import os
import shutil

#source path
path =  "C:/Users/vinod/Desktop/kanisshka/BFDI"

# to take input from user @ a destination directory
# dpath = input("enter the destination directory")


#Destination path
dpath= "C:Users/vinod/Desktop/kanisshka"

# Checking the list of files in it
print("Before copying files ,check them:")
print(os.listdir(path))

# to copy the file from source 2 destination
dest= shutil.copy(path,dpath)

# List of source folder after transfering teh file.
print("After copying file:")
print(os.listdir(path))
print(os.listdir(dpath))