from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import Seamcarving

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.resize)
        self.parent = parent
        self.initUI()
        self.flag=0
        self.img=None

    def resize(self,event):
        if self.flag>1 :
            self.img = Seamcarving.Run(self.img, (event.width, event.height))
            p=ImageTk.PhotoImage(self.img)
            self.label1.configure(image=p)
            self.label1.image = p
        self.flag += 1

    def initUI(self):
        self.parent.title("Seam Carving")
        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)
        fileMenu = Menu(menubar,tearoff=0)
        fileMenu.add_command(label = "Ouvrir une image", command = self.onOpen)
        menubar.add_cascade(label = "Image", menu = fileMenu)

    def setImage(self):
        if self.img is None:
            self.img = Image.open(self.fn)
            self.I = np.asarray(self.img)
            l, h = self.img.size
            self.parent.geometry("")
            if l > 1300:
                self.img.thumbnail((1300, h), Image.BICUBIC)
            if h > 600:
                self.img.thumbnail((l, 600), Image.BICUBIC)
            photo = ImageTk.PhotoImage(self.img)
            self.label1 = Label(self, border=0)
            self.label1.grid(row=1, column=0)
            self.label1.configure(image = photo)
            self.label1.image = photo
        else :
            self.img = Image.open(self.fn)
            self.I = np.asarray(self.img)
            l, h = self.img.size
            self.parent.geometry("")
            if l > 1300:
                self.img.thumbnail((1300, h), Image.BICUBIC)
            if h > 600:
                self.img.thumbnail((l, 600), Image.BICUBIC)
            p = ImageTk.PhotoImage(self.img)
            self.label1.configure(image=p)
            self.label1.image = p
        self.flag=1


    def onOpen(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png *.gif')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        self.fn = filename
        self.setImage()

def main():
    root = Tk()
    mycanvas = ResizingCanvas(root,width=700,height=500)
    mycanvas.pack(fill=BOTH, expand=1)
    root.mainloop()

if __name__ == "__main__":
    main()