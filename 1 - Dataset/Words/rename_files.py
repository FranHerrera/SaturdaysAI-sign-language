print("Init script to Rename all file for a FOLDER\n")
import os
print(" - Loaded os package\n")
path = input("  >> Please enter a path to rename files:\n")
print(" - Path set to: ", path)
word = input("  >> Please enter word name to replace (word-<word>-<number>.mp4):\n")
print(" - Word set to: ", word)

# Get all files for the selected path
file_list = os.listdir(path)
saved_path = os.getcwd()
print(" - Active folder is ", str(saved_path))
os.chdir(path)
# Loop to rename all files
i=1
for file_name in file_list :
    # New name with 3 digit start with 001 and end 999
    new_name = "word-{}-{}.mp4".format(word, str(i).zfill(3))
    print("     - Rename from ", file_name, " to ", new_name)
    os.rename(file_name, new_name)
    i=i+1
print("Finish script")
