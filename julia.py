from PIL import Image

# Constants
size = (2000,2000)
black = (0,0,0)
red = (255, 0,0)
white = (255,255,255)
bound = 10
iterations = 1000

# The point c of our quadratic julia funcion f_c = z^2 + c 
c = complex(-0.08,0.696)

# Creating the canvas
img = Image.new( 'RGB', size, "black") 
pixels = img.load()
print("Created canvas")

# Mapping from pixel to xy-plane
def pixel_to_xy(i,j):
    x = -2 + (4/size[0])*i
    y = 2 - (4/size[1])*j
    return( (x,y) )

# Function to check whether a point stays bounded or not
def Julia(x,y):
    z = complex(x,y)
    for _ in range(iterations):
        try:
            z = pow(z,2) + c # The quadratic map
        except:
            pass
        if abs(z) > bound:
            return z
    return z
    
# Loop through all pixels to colour them in correctly
for i in range(size[0]):   
    for j in range(size[1]):   
        coords = pixel_to_xy(i,j)
        result = Julia(coords[0], coords[1])
        norm = abs(result)
        if  norm < bound:
            pixels[i,j]  = black
        else:
            pixels[i,j] = white

# Showing and saving the picture
img.show()
img.save('images/julia3.png')
print("done!")
