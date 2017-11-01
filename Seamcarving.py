from tkinter.filedialog import askopenfilename
from PIL import Image
from math import *
import numpy as np


class Traitement:
    # les champs de la class :
    # private img : l'image


    def get_image(self):
        fname = askopenfilename()
        self.__img = Image.open(fname)

    def niveauGris(self):
        return self.__img.convert('L')


    def energy(self):
        im=self.niveauGris()
        (largeur, hauteur) = im.size
        tab = [[1000] * hauteur  for _ in range(largeur)]
        for i in range(1,largeur-1):
            for j in range(1,hauteur-1):
                x= im.getpixel((i-1,j-1))+2*im.getpixel((i-1,j))+im.getpixel((i-1,j+1))-im.getpixel((i+1,j-1))-2*im.getpixel((i+1,j))-im.getpixel((i+1,j+1))
                y= im.getpixel((i-1,j-1))+2*im.getpixel((i,j-1))+im.getpixel((i+1,j-1))-im.getpixel((i-1,j+1))-2*im.getpixel((i,j+1))-im.getpixel((i+1,j+1))
                tab[i][j]=sqrt((x*x)+(y*y))
        M = np.array(tab)
        return np.transpose(M).tolist()




    def getimg(self):
        return self.__img


    def chemin(self,tab):
        res=[]
        xmin= tab[1].index(min(tab[1]))
        res.append([xmin,1])
        for i in range(2,len(tab)-1):
            xmin=tab[i].index(min(tab[i][xmin-1],tab[i][xmin],tab[i][xmin+1]))
            res.append([xmin,i])
        return res

    def colpath(self,tab):
        for i,j in tab:
            self.__img.putpixel((i, j),0)


    def seam(self):
        self.get_image()
        tab = self.energy()
        path = self.chemin(tab)
        self.colpath(path)
        self.__img.save("E:/tt.jpg")




if __name__ == "__main__":
    t=Traitement()
    t.seam()


