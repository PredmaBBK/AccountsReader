from PIL import Image
import cv2
from matplotlib import pyplot as plt
import numpy as np


# Using PIL
im_file = "UI\\Reader\\TesseractTut\\TMS1.png"

im = Image.open(im_file)
# print(im)
# print(im.size)
# im.rotate(180).show()

# Using cv2
img = cv2.imread(im_file)
# cv2.imshow("Original image", img)
# cv2.waitKey(0)

# Displaying the image in the native window
def display_image(img):
    cv2.imshow(str(img), img)
    cv2.waitKey(0)

#displaying the image in line
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    height, width, depth = im_data.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width/float(dpi), height/float(dpi)

    # Create a figure of the right size with one axis which takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines and ticks
    ax.axis('off')

    # Display the image
    ax.imshow(im_data, cmap='gray')
    plt.show()



# Invert the image

inverted_image = cv2.bitwise_not(img)
cv2.imwrite("UI\\Reader\\TesseractTut\\inverted_image.png", inverted_image)
# display("UI\\Reader\\TesseractTut\\inverted_image.png")
# display_image(inverted_image)

# Greyscale
def greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_image = greyscale(img)
cv2.imwrite("UI\\Reader\\TesseractTut\\grey_image.png", grey_image)
# display_image(grey_image)

# Binarise
thresh, im_BW = cv2.threshold(grey_image, 140, 250, cv2.THRESH_BINARY)
cv2.imwrite("UI\\Reader\\TesseractTut\\bw_image.png", im_BW)
# display_image(im_BW)

# Removing noise
def noise_removal(image):
    
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    # image = cv2.medianBlur(image, 3)
    return (image)

no_noise = noise_removal(im_BW)
cv2.imwrite("UI\\Reader\\TesseractTut\\no_noise_image.png", no_noise)
# display_image(no_noise)


# For thin font
def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


# For thick font
def thicken_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


# display_image(thicken_font(no_noise))
# display_image(thin_font(no_noise))
# display_image(thin_font(thicken_font(no_noise)))


# Removing borders
def remove_borders(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contourSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    contour = contourSorted[-1]
    x, y, w, h = cv2.boundingRect(contour)
    crop = image[y:y+h, x:x+w]
    return crop

no_borders = remove_borders(no_noise)
cv2.imwrite("UI\\Reader\\TesseractTut\\no_borders_image.png", no_borders)
display_image(no_borders)



