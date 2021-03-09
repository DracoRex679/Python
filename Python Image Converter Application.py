import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python Image Converter')

def Convert(baseImgEntry, saveAsNameEntry, newImgTypeEntry, gTitleEntry):
    baseImg = baseImgEntry.get()
    saveAsName = saveAsNameEntry.get()
    newImgType = newImgTypeEntry.get()
    gTitle = gTitleEntry.get()
    
    img = mpimg.imread(baseImg)
    newImg = img[:,:,0]
    
    plt.ylabel("Height")
    plt.xlabel("Width")
    if newImgType == "spectral":
        plt.imshow(newImg[::-1], cmap="nipy_spectral", origin='lower')
    elif newImgType == "hot":
        plt.imshow(newImg[::-1], cmap="hot", origin='lower')
    elif newImgType == "luminous":
        plt.imshow(newImg[::-1], origin='lower')
    elif newImgType == "gray":
        plt.imshow(newImg[::-1], cmap='gray', origin='lower')
    elif newImgType == "twilight":
        plt.imshow(newImg[::-1], cmap='twilight', origin='lower')
    else:
        plt.imshow(img[::-1], origin='lower')        
    plt.colorbar()
    plt.title(gTitle)
    
    plt.savefig(saveAsName)
    
    plt.show()

label = Label(root, borderwidth=5, text="Enter an image or image location for the new graph (Please end image in file type Ex. .png): ")
label.grid(row=0, column = 0, columnspan=5)

baseImgEntry = Entry(root, borderwidth=5)
baseImgEntry.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

label = Label(root, borderwidth=5, text="What would you like to save the image as (Please include file type Ex. .png): ")
label.grid(row=2, column = 0, columnspan=5)

saveAsNameEntry = Entry(root, borderwidth=5)
saveAsNameEntry.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

label = Label(root, borderwidth=5, text="What kind of image do you want (luminous, gray, hot, spectral, twilight): ")
label.grid(row=4, column = 0, columnspan=5)

newImgTypeEntry = Entry(root, borderwidth=5)
newImgTypeEntry.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

label = Label(root, borderwidth=5, text="What would you like to title the graph?: ")
label.grid(row=6, column = 0, columnspan=5)

gTitleEntry = Entry(root, borderwidth=5)
gTitleEntry.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

button = Button(root, text="Enter", command = lambda: Convert(baseImgEntry, saveAsNameEntry, newImgTypeEntry, gTitleEntry))
button.grid(row=8, column=2)

root.mainloop()