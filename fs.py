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
    def __init__(self, path, filenameExten = None, fulldirlist = None):
       
        self.path = path
        self.fne = filenameExten

        self.filelist = [f for f in os.listdir(path) if
                os.path.isfile(os.path.join(path, f))]

        if fulldirlist == None:
            self.subdir = [f for f in os.listdir(path) if
                    os.path.isdir(os.path.join(path, f))
                    ]
            self.fulldir = [self.get_dirpath(i) for i in range(len(self.subdir))]
        else:
            self.fulldir = fulldirlist
            print (self.fulldir[0])
            forre = ".+/(.+)$"
            self.subdir = [(re.match(forre ,self.fulldir[i])).group(1) for i
                     in range(len(self.fulldir))]


        if self.fne != None:
            forRe = ".*\." + self.fne + "$" # like".*\.py$"

            self.filelist = [f for f in self.filelist if
                  re.match(forRe, f)  ]

    def moveFile(self, fileIndex, dirIndex):
   
        if not(self.file_empty()):
            oldfile = self.path + "/" + self.filelist[fileIndex]
            newfile = self.fulldir[dirIndex] + "/" + self.filelist[fileIndex]
            shutil.move(oldfile, newfile)

    def get_filepath(self, fileIndex):

        if(len(self.filelist)==0):
            return None
        else:
            return self.path + "/" + self.filelist[fileIndex]

    # It's function have some problem
    def get_dirpath(self, dirIndex):

        if(len(self.subdir)==0):
            return None
        else:
            return self.path + "/" + self.subdir[dirIndex]

    def refresh(self, dirlist = None):

        self.filelist = [f for f in os.listdir(self.path) if
                os.path.isfile(os.path.join(self.path, f))]

        if self.fne != None:
            forRe = ".*\." + self.fne + "$" # like".*\.py$"

            self.filelist = [f for f in self.filelist if
                re.match(forRe, f)  ]

        if dirlist != None:
            self.fulldir = dirlist

            forre = ".+/(.+)$"
            self.subdir = [re.match(forre ,self.fulldir[i]).group(1)
                    for i in range(len(self.fulldir))
                    if re.match(forre, self.fulldir[i])]

    def file_empty(self):

        return not(bool(len(self.filelist)))

# if __name__ == "__main__":

    # path = "C:/Users/a2395/Desktop/fortest"

    # fulldir = ["C:/Users/a2395/Desktop/fortest/1" ,
            # "C:/Users/a2395/Desktop/fortest/2","C:/Users/a2395/Desktop/fortest/3"]

    # fs = filesystem(path = path, filenameExten = "txt", fulldirlist = fulldir)

    # print(fs.subdir)


