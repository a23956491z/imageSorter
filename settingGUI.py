from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from fs import filesystem

class settingFrame(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.grid()

        self.autoloadBut = Button(self, text = "Auto Load",
                                  command = self.auto_load)
        self.autoloadBut.grid(row = 0, column = 0, pady = (10,10), padx = (10,10))

        self.saveBut = Button(self, text = "Save")
        self.saveBut.grid(row = 0, column = 1, pady = (10,10), padx = (0,10))

        self.pathLab = Label(self, text = "Path : ")
        self.pathLab.grid(row = 1, column = 0, pady = (0,10), padx = (10,10))
        self.pathEnt = Entry(self, width = 40)
        self.pathEnt.grid(row = 1, column = 1, pady = (0,10), padx = (0,10))
        self.pathBut = Button(self, text = "Select", command = self.select_path)
        self.pathBut.grid(row = 1, column = 2, pady = (0,10), padx = (0,10))

        self.dirpathLabList = [Label(self, text = "folder{0} : ".format(i + 1)) 
             for i in range(10)]
        for i in range(len(self.dirpathLabList)):
            self.dirpathLabList[i].grid(row = 2 + i, column = 0,
                                     pady = (0,10), padx = (10,10))

        self.dirpathEntList = [Entry(self, width = 40) for i in range(10)]
        for i in range(len(self.dirpathEntList)):
            self.dirpathEntList[i].grid(row = i + 2, column = 1,
                                    pady = (0,10), padx = (0,10))

        self.selectButList = [Button(self, text = "Select", 
            command = lambda idx = i:self.select_dir(idx)) for i in range(10)]

        for i in range(len(self.selectButList)):
            self.selectButList[i].grid(row = i + 2, column = 2,
                                       pady = (0,10), padx = (0,10))

    def select_path(self):

        options = {'title' : "Select a directroy"}
        new_path = filedialog.askdirectory(**options)
        
        if new_path:
            self.pathEnt.delete(0, END)
            self.pathEnt.insert(0, new_path)

    def select_dir(self, idx):
        
        options = {'title' : "Select a directroy"}
        dirpath = filedialog.askdirectory(**options)
        
        if dirpath:
            self.dirpathEntList[idx].delete(0, END)
            self.dirpathEntList[idx].insert(0,dirpath)

    def auto_load(self):
        
        self.path = self.pathEnt.get()
        self.fs = filesystem(self.path)

        if self.path:
            for i in range(len(self.fs.subdir)):
                self.dirpathEntList[i].delete(0, END)
                self.dirpathEntList[i].insert(0, self.fs.get_dirpath(i))
        


if __name__ == "__main__":
    
    root = Tk()
    setting1 = settingFrame(root)

    setting1.mainloop() 
