import os
folders = input("please provide list of folders: ").split()

for folder in folders:

    try:

      files = os.listdir(folder)
    except FileNotFoundError:
      print("please provide a valid folder name")
      break

    print("============listing of files for the folder - " + folder)
    for file in files:
        print(file)