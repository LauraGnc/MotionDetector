# this script will resize images in a directory.
'''You can change some parameters to change the values of the resized size, and also
specify the formats of the images. If you want the images to be resized and to be
in black and white, change the value in line 14 from 1 to 0.'''


import cv2
import glob

# Store the img in a LIST:
listi = glob.glob('*.jpg')

for i in listi:
    img = cv2.imread(i, 0) # [0] for B&W ||| 1 to keep the colors.
    re = cv2.resize(img, (200, 200)) # Change the resized values here!
    nw = cv2.imwrite('resized_'+i, re)