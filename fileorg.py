import os
from pathlib import Path
import shutil

from datetime import date
from datetime import datetime

todays_date = date.today()
res = todays_date.strftime("%B")
month = str(res)
year = todays_date.year
#Can also get year like this:
#year = datetime.now().year

#This line of code is to print working directory:
#print(os.getcwd())

#Changing directory to here, Notice the FORWARD slashes:
os.chdir('/Users/akv/Downloads')

#pwd here again:
#print(os.getcwd())
#To print ls the items in this directory
#print(os.listdir())
#To get the unique list of file types in your directory:
'''
target_folder = '/Users/akv/Downloads'
extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}
print(extensions)
'''

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", "apng", ".avif", ".PNG")

pdf = (".pdf", ".PDF")

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

if not os.path.exists(str(month) + " " + str(year) + " Balance Sheet"):
    os.mkdir(str(month) + " " + str(year) + " Balance Sheet")

for file in os.listdir():
    if is_image(file):
        shutil.move(file, '/Users/akv/Documents')
    elif is_pdf(file):
        shutil.move(file, str(month) + " " + str(year) + " Balance Sheet")
    



