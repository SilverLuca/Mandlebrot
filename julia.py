from PIL import Image

size = (1024,1024)
black = (0,0,0)
red = (255, 0,0)
bound = 10


iterations = 100

img = Image.new( 'RGB', size, "black") 
pixels = img.load() 

def pixel_to_xy(i,j):
    x = -2 + (4/size[0])*i
    y = 2 - (4/size[1])*j
    return( (x,y) )
    
def mandelbrotfunc(x,y):
    z = complex(x,y)
    for _ in range(iterations):
        try:
            z = z - (pow(z,3) -1)/(2*pow(z,2))
        except:
            pass
        if abs(z) > bound:
            return z
    return z
    
#print(mandelbrotfunc(0,0.5))

for i in range(size[0]):    # for every col:
    for j in range(size[1]):    # For every row
        coords = pixel_to_xy(i,j)
        result = mandelbrotfunc(coords[0], coords[1])
        norm = abs(result)
        if  norm < 10:
            pixels[i,j]  = black
        else:
            pixels[i,j] = red
    #print(f'The image is {100/size[0]*i}% done')

img.show()

img.save('images/julia.png')
print("done!")
