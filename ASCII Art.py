from PIL import Image, ImageFilter
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#File chooser dialog window
Tk().withdraw() #gets rid of root window
filename = askopenfilename() 

#loads image
im = Image.open(filename).convert('RGB')

#2D array setup
cols=im.height+1
rows=im.width+1
arr=[[0]*cols]*rows

#storing tuples of each pixel of the picture in 2D array
for y in range(im.height):
    print("\n")
    for x in range(im.width):
        arr[x][y]=im.getpixel((x,y))

        #convert RGB tuples of each pixel to brightness values
        temp_tuple=arr[x][y]
        brightness_value=0.21*temp_tuple[0] + 0.72*temp_tuple[1] + 0.07*temp_tuple[2] #take a weighted average of the R, G and B values to account for human perception
        
        #convert brightness values to ASCII characters
        ascii_list="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" 
        ascii_index=(round(brightness_value/3.98))
        symbol=ascii_list[ascii_index]

        #prints ASCII characters
        print(symbol, end="")
        print(symbol, end="")
        print(symbol, end="")