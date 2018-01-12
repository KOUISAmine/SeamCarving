from PIL import Image
from scipy.ndimage.filters import generic_gradient_magnitude, sobel
import numpy

def filter_gradient(img):
    im=img.convert("F")
    im_width, im_height = im.size
    im_arr = numpy.reshape(im.getdata(), (im_height, im_width))
    sobel_arr = generic_gradient_magnitude(im, derivative=sobel)
    gradient = Image.new("F", im.size)
    gradient.putdata(list(sobel_arr.flat))
    return gradient


def img_transpose(im):

    im_width, im_height = im.size
    im_arr = numpy.reshape(im.getdata(), (im_height, im_width))
    im_arr = numpy.transpose(im_arr)
    im = Image.new(im.mode, (im_height, im_width))
    im.putdata(list(im_arr.flat))
    return im


def chercher_chemin_horizontal(im):

# im est l'application du filter gradient sur l'image

    im_width, im_height = im.size

    cost = numpy.zeros(im.size)

    im_arr = numpy.reshape(im.getdata(), (im_height, im_width))
    im_arr = numpy.transpose(im_arr)
    for y in range(im_height):
        cost[0, y] = im_arr[0, y]


    for x in range(1, im_width):

        for y in range(im_height):
            if y == 0:
                min_val = min(cost[x - 1, y], cost[x - 1, y + 1])
            elif y < im_height - 2:
                min_val = min(cost[x - 1, y], cost[x - 1, y + 1])
                min_val = min(min_val, cost[x - 1, y - 1])
            else:
                min_val = min(cost[x - 1, y], cost[x - 1, y - 1])
            cost[x, y] = im_arr[x, y] + min_val

    min_val = 1e1000
    path = []

    for y in range(im_height):
        if cost[im_width - 1, y] < min_val:
            min_val = cost[im_width - 1, y]
            min_ptr = y

    pos = (im_width - 1, min_ptr)
    path.append(pos)

    while pos[0] != 0:
        val = cost[pos] - im_arr[pos]
        x, y = pos
        if y == 0:
            if val == cost[x - 1, y + 1]:
                pos = (x - 1, y + 1)
            else:
                pos = (x - 1, y)
        elif y < im_height - 2:
            if val == cost[x - 1, y + 1]:
                pos = (x - 1, y + 1)
            elif val == cost[x - 1, y]:
                pos = (x - 1, y)
            else:
                pos = (x - 1, y - 1)
        else:
            if val == cost[x - 1, y]:
                pos = (x - 1, y)
            else:
                pos = (x - 1, y - 1)

        path.append(pos)

    return path


def chercher_chemin_vertical(im):
    # im est l'application du filter gradient sur l'image
    im = img_transpose(im)
    u = chercher_chemin_horizontal(im)
    for i in range(len(u)):
        temp = list(u[i])
        temp.reverse()
        u[i] = tuple(temp)
    return u



def supp_chemin_horizontal(img, path):

    img_width, img_height = img.size
    i = Image.new(img.mode, (img_width, img_height - 1))
    input = img.load()
    output = i.load()
    path_set = set(path)
    seen_set = set()
    for y in range(img_height):
        for x in range(img_width):
            if (x, y) not in path_set and x not in seen_set:
                output[x, y] = input[x, y]
            elif (x, y) in path_set:
                seen_set.add(x)
            else:
                output[x, y - 1] = input[x, y]

    return i


def supp_chemin_vertical(img, path):

    img_width, img_height = img.size
    i = Image.new(img.mode, (img_width - 1, img_height))
    input = img.load()
    output = i.load()
    path_set = set(path)
    seen_set = set()
    for x in range(img_width):
        for y in range(img_height):
            if (x, y) not in path_set and y not in seen_set:
                output[x, y] = input[x, y]
            elif (x, y) in path_set:
                seen_set.add(y)
            else:
                output[x - 1, y] = input[x, y]

    return i

def Run(input, resolution):

    im_width, im_height = input.size

    while im_width > resolution[0]:
        u = chercher_chemin_vertical(filter_gradient(input))
        input = supp_chemin_vertical(input, u)
        im_width = input.size[0]

    while im_height > resolution[1]:
        v = chercher_chemin_horizontal(filter_gradient(input))
        input = supp_chemin_horizontal(input, v)
        im_height = input.size[1]

    return input