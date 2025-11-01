import sys
import math
import random
import time
from PIL import Image

def make_grad_matrix(size,num):
    a=list()
    for i in range(num+1):
        a.append(list())
        for j in range(num+1):
            grad_vec = (random.random(),random.random())
            a[i].append(grad_vec)
    return a
def fade(t):
    """6t^5 - 15t^4 + 10t^3"""
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def dot(g, x, y):
    return g[0]*x + g[1]*y

def perlin(x, y, g00, g10, g01, g11):
    X = int(math.floor(x))
    Y = int(math.floor(y))
    dx = x - math.floor(x)
    dy = y - math.floor(y)

    n00 = dot(g00, dx, dy)
    n10 = dot(g01, dx - 1, dy)
    n01 = dot(g10, dx, dy - 1)
    n11 = dot(g11, dx - 1, dy - 1)

    u = fade(dx)
    v = fade(dy)

    nx0 = lerp(n00, n10, u)
    nx1 = lerp(n01, n11, u)
    return lerp(nx0, nx1, v)

def make_image(size, Gmatrix, Num):
    img = Image.new("L", (size, size))
    pix = img.load()

    split_size = int(math.ceil(size//Num))
    for j in range(size):
        for i in range(size):
            val = perlin(i/split_size, j/split_size, Gmatrix[j//split_size][i//split_size],Gmatrix[j//split_size+1][i//split_size],Gmatrix[j//split_size][i//split_size+1],Gmatrix[j//split_size+1][i//split_size+1])

            gray = int((val + 1) * 127.5)
            pix[i, j] = gray
    return img

def make_matrix(size, Gmatrix, Num):
    f = open(f"./martix_{size}_{Num}",mode='w')
    split_size = size//Num
    for j in range(size):
        for i in range(size):
            val = perlin(i/split_size, j/split_size, Gmatrix[j//split_size][i//split_size],Gmatrix[j//split_size+1][i//split_size],Gmatrix[j//split_size][i//split_size+1],Gmatrix[j//split_size+1][i//split_size+1])

            f.write(str(val))
            f.write(' ')
        f.write("\n")
    return

def generate_picture(size, Gmatrix, Num_of_box):
    img = make_image(size, Gmatrix, Num_of_box)
    fname = f"perlin_{size}_{Num_of_box}.png"
    img.save(fname)

    img.show(title='perlin_noise')
    print(f"已生成 {fname}  ({size}×{size})\ngenerated {fname}  ({size}×{size})")

def generate_matrix(size, Gmatrix, Num_of_box):
    img = make_matrix(size, Gmatrix, Num_of_box)

def main():
    if len(sys.argv) != 4:
        print("Usage: python perlin_png.py <mode> <size> <lattice>\nmode: m=matrix p=picture\nsize:output size=(2^size, 2^size)")
        sys.exit(1)
    n = int(sys.argv[2])
    Num_of_box = int(sys.argv[3])
    m = str(sys.argv[1])
    size = 2**n

    Gmatrix = make_grad_matrix(size, Num_of_box)
    if(m=="p"):
        generate_picture(size, Gmatrix, Num_of_box)
    if(m=="m"):
        generate_matrix(size, Gmatrix, Num_of_box)

if __name__ == "__main__":
    main()