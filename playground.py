import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

# This function will allow the user to select all pictures and restricts it only to png and jpeg files
def getFiles():
    fileTypes = [("PNG", "*.png"),
                 ("JPEG", "*.jpg")]
    currdir = os.getcwd()
    allFiles = filedialog.askopenfilenames(parent=root, initialdir=currdir, title='Please select files', filetypes=fileTypes)
    if len(allFiles) > 0:
        for name in allFiles:
            print ("File path: ", name)


getFiles()
"""file_path_variable = search_for_file_path()
print ("\nfile_path_variable = ", file_path_variable)"""