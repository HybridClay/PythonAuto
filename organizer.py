#From YT: "Code With Me: Automating my Life With Python | Build a file organizer" by Tiff in Tech

import os     #For being able to acces files in directories
import shutil #To be able to move files around

#using expanduser lets us to not have to write the whole directory path
directory = os.path.join(os.path.expanduser("~"), "Downloads")

#Here you would write the extension path and to which folder to be placed in
#The folders will be created in the code
extensions = {
    '.jpg': 'pics',
    '.jpeg': 'pics',
    '.png': 'pics',
    '.gif': 'pics',
    '.mp4': 'vids',
    '.avi': 'vids',
    '.mov': 'vids',
    '.doc': 'Docs',
    '.docx': 'Docs',
    '.pdf': 'Docs',
    '.txt': 'Docs',
    '.mp3': 'music',
    '.wav': 'music',
    '.xlsx': 'excel'
}

for filename in os.listdir(directory):      #Here we go through each file inside the directory
    file_path = os.path.join(directory, filename)   #Here we have the path of that file put in the variable file_path 

    if os.path.isfile(file_path):       #Here we check if its a file in the file path
        extension = os.path.splitext(filename)[1].lower()   #If it is a file, then take its extension part

        if extension in extensions:   #If its extension part is in our dictionary of extensions then...
            folder_name = extensions[extension] #Have a folder_name varibale made to contain the value associated with extensions[extension] key in key-value pair

            folder_path = os.path.join(directory, folder_name) # Here we have the path of that folder directory in the varibale folder_path
            os.makedirs(folder_path, exist_ok=True) #Here the folder directory (to which the dictionarie key value pair is associated with) is created

            destination_path = os.path.join(folder_path, filename) #Here we create a path to where the file will go
            shutil.move(file_path, destination_path) #Here We move the file to where it needs to go in

            print(f"Moved {filename} to {folder_name} folder.") #This prints to let us know what file was moved to which folder
        else:
            print(f"Skipped {filename}. Unknown file extension.") #This lets us know which files were skipped becuase they were not listed in our dictionary collection
    else:                              #If its not a file then we skip it because its actually a directory
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.") #When its finished going through the files in the directory, print this
