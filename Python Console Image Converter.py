import matplotlib.pyplot as plt
import matplotlib.image as mpimg

baseImg = input("Enter an image or image location for the new graph (Please end image in file type Ex. .png): ")
saveAsName = input("What would you like to save the image as (Please include file type Ex. .png): ")
newImgType = input("What kind of image do you want (luminous, gray, hot, spectral, twilight): ")
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
gTitle = input("What would you like to title the graph?: ")
plt.title(gTitle)
plt.savefig(saveAsName)