#This code works with folder directories conataining FILES ONLY (like Downloads folder)
#Downloads folder has Files Only

import os
import shutil

from datetime import date

todays_date = date.today()
res = todays_date.strftime("%B")
month = str(res)
year = todays_date.year

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".PNG")

pdf = (".pdf")

excel = (".xlsx")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".svg", ".apng", ".mxf")


def is_image(file):
    return os.path.splitext(file)[1] in img

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

def is_excel(file):
    return os.path.splitext(file)[1] in excel

def is_video(file):
    return os.path.splitext(file)[1] in video


os.chdir("/Users/UsersNameHere/Documents") #Here we change to the Documents directory
#Then we create these folder directories if they are not yet created in Documents folder
if not os.path.exists(str(month) + " " + str(year) + " Balance Sheets"):
    os.mkdir(str(month) + " " + str(year) + " Balance Sheets")
if not os.path.exists(str(month) + " " + str(year) + " Excel GSheets"):
    os.mkdir(str(month) + " " + str(year) + " Excel GSheets")

os.chdir('C:/Users/UsersNameHere/Pictures') #Then we change to the Pictures directory and create this folder if not yet created
if not os.path.exists(str(month) + " " + str(year) + " Balance Sheets Texted"):
    os.mkdir(str(month) + " " + str(year) + " Balance Sheets Texted")

os.chdir('C:/Users/UsersNameHere/Downloads') #Then we change to the Downloads directory
# We will check each file item and move them to the folder they belong to
for file in os.listdir():
    if is_image(file):
        shutil.move(file, 'C:/Users/UsersNameHere/Pictures/' + str(month) + " " + str(year) + " Balance Sheets Texted")
        print("All images in Downloads moved to Pictures directory")
    elif is_pdf(file):
        shutil.move(file, 'C:/Users/UsersNameHere/Documents/' + str(month) + " " + str(year) + " Balance Sheets")
        print("All pdf Balance Sheets moved to Documents directory in their respective Date folder")
    elif is_excel(file):
        shutil.move(file, 'C:/Users/UsersNameHere/Documents/' + str(month) + " " + str(year) + " Excel GSheets")
    elif is_video(file):
        shutil.move(file, 'C:/Users/UsersNameHere/Documents')

print("Finished organizing files Boss!  :D  ")
