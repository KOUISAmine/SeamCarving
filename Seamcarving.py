from tkinter.filedialog import askopenfilename
from PIL import Image
from skimage import img_as_float
from skimage import filter
from math import *
import numpy as np
global q

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


		def dual_gradient_energy(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    hR = filter.hsobel(R)
    hG = filter.hsobel(G)
    hB = filter.hsobel(B)

    vR = filter.vsobel(R)
    vG = filter.vsobel(G)
    vB = filter.vsobel(B)

    sumRG = np.add(np.square(hR), np.square(hG))
    x_square = np.add(sumRG, np.square(hB))

    sumRGv = np.add(np.square(vR), np.square(vG))
    y_square = np.add(sumRGv, np.square(vB))

    energy = np.add(x_square, y_square)
    return energy
		
		
	def remove_seam(img, minIndex, sOfIJ):
		rows = img.shape[0]
		columns = img.shape[1]
		removed_matrix = np.zeros(shape=(rows, columns - 1, 3))
		k = minIndex
		# backtracking from last row to first row
		for i in range(rows - 1, -1, -1):
			b = img[i, :, :]  # taking one by one row from img matrix
			# deleting kth position in a row
			removed_matrix[i, :, :] = np.delete(b, k, axis=0)
			if i != 0:
				if k == 1:
					if sOfIJ[i - 1, k + 1] < sOfIJ[i - 1, k]:
						k = k + 1
				elif k == columns - 2:
					if sOfIJ[i - 1, k - 1] < sOfIJ[i - 1, k]:
						k = k - 1
				else:
					if sOfIJ[i - 1, k - 1] < sOfIJ[i - 1, k] and sOfIJ[i - 1, k - 1] < sOfIJ[i - 1, k + 1]:
						k = k - 1
					elif sOfIJ[i - 1, k + 1] < sOfIJ[i - 1, k] and sOfIJ[i - 1, k + 1] < sOfIJ[i - 1, k - 1]:
						k = k + 1
		return removed_matrix
		pass

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


    def seam(self):
	    img = imread('givenImg.png')
		img = img_as_float(img)
		subplot(1, 3, 1)
		imshow(imread('givenImg.png'))
		title('Given')
		figure()
		gray()
        self.get_image()
        tab = self.energy()
        path = self.chemin(tab)
        self.colpath(path)
        self.__img.save("E:/tt.jpg")




if __name__ == '__main__':
    main()


