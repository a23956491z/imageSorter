import os
from PIL import Image, ImageTk
import inspect
import re
import shutil

class picture:
    def __init__(self, path):

        self.image = Image.open(path)

        tempWidth, tempHeight = self.image.size
        self.ratio = tempHeight / float(tempWidth)

    def resize(self, width, height, lockmode = None):

        if lockmode == "height":
            new_width = height / self.ratio
            self.image = self.image.resize((int(new_width), height), Image.BILINEAR)

        elif lockmode == "width":
            new_height = self.ratio * width
            self.image = self.image.resize((width, int(new_height)), Image.BILINEAR)

        elif lockmode == None:
            self.image = self.image.resize((height, width), Image.BILINEAR)
        
    def get_tk(self):

        return ImageTk.PhotoImage(self.image)

    def get_size(self):

        return self.image.size

class filesystem:
    def __init__(self, path, filenameExten = None):
       
        self.path = path

        self.filelist = [f for f in os.listdir(path) if
                os.path.isfile(os.path.join(path, f))]

        self.subdir = [f for f in os.listdir(path) if
                os.path.isdir(os.path.join(path, f))]
        
        self.fne = filenameExten

        if filenameExten != None:
            forRe = ".*\." + self.fne + "$" # like".*\.py$"

            self.filelist = [f for f in self.filelist if
                  re.match(forRe, f)  ]

    def moveFile(self, fileIndex, dirIndex):
    
        oldfile = self.path + "/" + self.filelist[fileIndex]
        newfile = self.path + "/" + self.subdir[dirIndex] + "/" + self.filelist[fileIndex]
        shutil.move(oldfile, newfile)

    def get_filepath(self, fileIndex):

        if(len(self.filelist)==0):
            return None
        else:
            return self.path + "/" + self.filelist[fileIndex]

    def get_dirpath(self, dirIndex):

        if(len(self.subdir)==0):
            return None
        else:
            return self.path + "/" + self.subdir[dirIndex]

    def refresh(self):

        self.filelist = [f for f in os.listdir(self.path) if
                os.path.isfile(os.path.join(self.path, f))]

        self.subdir = [f for f in os.listdir(self.path) if
                os.path.isdir(os.path.join(self.path, f))]

# if __name__ == "__main__":

    # path = "C:/Users/a2395/Desktop/fortest"

    # fs = filesystem(path = path, filenameExten = "txt")

    # fs.moveFile(0, 0)

    # print fs.filelist
    # print fs.subdir
