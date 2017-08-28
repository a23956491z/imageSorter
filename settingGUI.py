from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox

from fs import filesystem

from pynput import keyboard

class settingFrame(Toplevel):

    def __init__(self, master = None):
        Toplevel.__init__(self, master)
        self.parent = master
        
        self.create_widget()

        self.push_keyBut_sign = False
        self.bind("<Key>", self.key)

    def create_widget(self):

        self.autoloadBut = Button(self, text = "Auto Load",
                                  command = self.auto_load)
        self.autoloadBut.grid(row = 0, column = 0, pady = (10,10), padx = (10,10))

        self.saveBut = Button(self, text = "Save", command = self.push_save)
        self.saveBut.grid(row = 0, column = 1, pady = (10,10), padx = (0,10))

        self.pathLab = Label(self, text = "Path : ")
        self.pathLab.grid(row = 1, column = 0, pady = (0,10), padx = (10,10))
        self.pathEnt = Entry(self, width = 40)
        self.pathEnt.insert(END, self.parent.settingPath)
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
        for entry, fulldir in zip(self.dirpathEntList, self.parent.settingFulldir):
            entry.insert(END, fulldir)

        self.selectButList = [Button(self, text = "Select", 
            command = lambda idx = i:self.select_dir(idx)) for i in range(10)]

        for i in range(len(self.selectButList)):
            self.selectButList[i].grid(row = i + 2, column = 2,
                                       pady = (0,10), padx = (0,10))

        self.keyButList = [Button(self, 
            text = "Key : {0}".format(self.master.keybind[i]),
            command = lambda idx = i : self.push_keyBut(idx)) for i in range(10)]
        
        for i in range(len(self.keyButList)):
            self.keyButList[i].grid(row = i + 2, column = 3,
                                    pady = (0,10), padx = (0,10))
        

    def select_path(self):

        options = {'title' : "Select a directroy"}
        new_path = filedialog.askdirectory(**options)
        
        if new_path:
            self.pathEnt.delete(0, END)
            self.pathEnt.insert(0, new_path)
            self.path = self.pathEnt.get()

    def select_dir(self, idx):
        
        options = {'title' : "Select a directroy"}
        dirpath = filedialog.askdirectory(**options)
        
        if dirpath:
            self.dirpathEntList[idx].delete(0, END)
            self.dirpathEntList[idx].insert(0,dirpath)

    def auto_load(self):
        
        self.path = self.pathEnt.get()

        if(len(self.path) == 0):
            messagebox.showerror("Error!", "The path is empty!")

        self.fs = filesystem(self.path)

        if self.path:
            for i in range(10):
                self.dirpathEntList[i].delete(0, END)
            for i in range(len(self.fs.subdir)):
                self.dirpathEntList[i].insert(0, self.fs.get_dirpath(i))
        
    def push_save(self):

        self.path = self.pathEnt.get()
        self.parent.fs.path = self.path
        self.parent.settingPath = self.path

        
        dirlist = []
        for l in self.dirpathEntList:
            dirlist.append(l.get())
        
        self.parent.settingFulldir = dirlist

        if(not(len(dirlist))):
            messagebox.showerror("Error!", "The path of floders for sorting is empty!!")
        

        
        self.parent.fs.refresh(dirlist)
        self.parent.update()

    def push_keyBut(self, idx):

        self.push_keyBut_sign = True
        self.keyButIndex = idx
        self.keyButList[idx]["text"] = "Press Key"
        
    def key(self, event):
        
        if self.push_keyBut_sign:
            self.push_keyBut_sign = False
            now_key = event.keysym

            self.master.keybind[self.keyButIndex] = now_key
            self.keyButList[self.keyButIndex]["text"] = "Key : {0}".format(now_key)


if __name__ == "__main__":
    
    root = Tk()
    setting1 = settingFrame(root)

    setting1.mainloop() 
