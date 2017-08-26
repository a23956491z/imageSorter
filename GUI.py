from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
from fs import picture,filesystem
from settingGUI import settingFrame
class mainFrame(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)


        self.note = Notebook(master)
        self.note.pack(padx = (10, 10), pady = (10, 10))

        self.tab1 = Frame(self.note)
        self.tab2 = Frame(self.note)
        self.tab3 = Frame(self.note)

        self.note.add(self.tab1, text = "Tab One")
        self.note.add(self.tab2, text = "Tab Two")
        self.note.add(self.tab3, text = "Tab Three")


        self.buttonList = [Button(self.tab1, text =
            "Empty", command = lambda idx = i :self.push_dir(idx)) for i in range(10) ]
        

        i = 0
        for but in self.buttonList:
            but.grid(row = 0, column = i, pady = (10,10), padx = (10,0) if i ==
                    0 else (0,0))
            i += 1

        self.setting = Button(self.tab1, text = "setting",
                              command = self.open_setting)
        self.setting.grid(row = 1, column = 8, columnspan = 2)
       
        self.refreshBut = Button(self.tab1, text = "refresh",
                                 command = self.update)
        self.refreshBut.grid(row = 1, column = 7, columnspan = 2)

        self.now_path = "C:/Users/a2395/Desktop/fortest"
        self.fs = filesystem(self.now_path, "jpg")

        self.settingPath = self.now_path
        self.settingFulldir = self.fs.fulldir

        self.set_pic(1)

        self.path = Label(self.tab1, text = self.now_path, wraplength = 600)
        self.path.grid(row = 1, column = 0, columnspan = 8)

        self.filename = Label(self.tab1, text = self.fs.filelist[0],  wraplength = 125)
        self.filename.grid(row = 2, column = 8, columnspan = 2
                          ,padx = (10,2), pady = (10,10))
        
        self.list = Listbox(self.tab1, height = 30)
        self.list.grid(row = 3, column = 8, columnspan = 2, rowspan = 8, padx = (10,2))
        
        for file in self.fs.filelist:
            self.list.insert(END, file) 

    def dir_to_button(self, dirlist):

        tempdir = [i for i in dirlist]

        for but in self.buttonList:
            but["text"] = "Empty"
        for but, dir in zip(self.buttonList, tempdir):
            but["text"] = dir[:9]

    def push_dir(self, idx):

        self.fs.moveFile( 0, idx)
        self.fs.refresh()
        self.set_pic()

        self.list.delete(0)
        self.filename["text"] = self.fs.filelist[0]

    def set_pic(self, init = 0):

        pic = picture(self.fs.get_filepath(0))
        temp_width, temp_height = pic.get_size()

        if(temp_width > temp_height):
            pic.resize(700,700, "width")
        else:
            pic.resize(700,700, "height")
    
        self.dir_to_button(self.fs.subdir)

        self.imageObj = pic.get_tk()

        if init:
            self.panel = Label(self.tab1, image = self.imageObj)
            self.panel.grid(row = 2, column = 0, columnspan = 9, rowspan = 9
                       ,padx = (2, 60), pady = (10, 10))
        else:
            self.panel["image"] = self.imageObj

    def update(self):
        
        self.fs.refresh()
        self.now_path = self.fs.path

        self.path["text"] = self.now_path 

        self.filename["text"] = self.fs.filelist[0]

        
        self.list.delete(0, END)
        
        for file in self.fs.filelist:
            self.list.insert(END, file) 

        self.set_pic(0)

    def open_setting(self):

        setting = settingFrame(self)
        setting.grab_set()

if __name__ == "__main__":
    
    root = Tk()
    mainwin = mainFrame(root)

    mainwin.mainloop()
        
