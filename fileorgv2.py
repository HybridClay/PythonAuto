#Creating a file organizer in a Folder directory containing Files AND Folders

import os     
import shutil 

from datetime import date

todays_date = date.today()
res = todays_date.strftime("%B")
month = str(res)
year = todays_date.year

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    '.jpg': 'pics',
    '.jpeg': 'pics',
    '.png': 'pics',
    '.gif': 'pics',
    'jfif': 'pics',
    '.doc': 'Docs',
    '.docx': 'Docs',
    '.txt': 'Docs',
    '.pdf': str(month) + " " + str(year) + " Balance Sheets",
    '.xlsx': 'excel Google Sheets'
}

for filename in os.listdir(directory):      
    file_path = os.path.join(directory, filename)   

    if os.path.isfile(file_path):       
        extension = os.path.splitext(filename)[1].lower()   

        if extension in extensions:   
            folder_name = extensions[extension] 

            folder_path = os.path.join(directory, folder_name) 
            os.makedirs(folder_path, exist_ok=True) 

            destination_path = os.path.join(folder_path, filename) 
            shutil.move(file_path, destination_path) 

            print(f"Moved {filename} to {folder_name} folder.") 
        else:
            print(f"Skipped {filename}. Unknown file extension.") 
    else:                             
        print(f"Skipped {filename}. It is a directory.")

print("Images in Pictures directory organization completed!  :)") 

