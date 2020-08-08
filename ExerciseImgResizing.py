# this script will resize images in a directory.
'''You can change some parameters to change the values of the resized size, and also
specify the formats of the images. If you want the images to be resized and to be
in black and white, change the value in line 14 from 1 to 0.'''

# The picture(s) need to be in the same directory as the script.


import cv2
import glob

# Store the img in a LIST:
listi = glob.glob('*.png')

for i in listi:
    img = cv2.imread(i, 1) # [0] for B&W ||| 1 to keep the colors.
    # re = cv2.resize(img, (500, 300)) # Change the resized values here!

    # Resize your image by percentage with the following snippet
    re = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))
    nw = cv2.imwrite('resized_'+i, re)