import os
import cv2
import sys
import FocusStack
from read_images import ImageReader
"""

    Focus stack driver program

    This program looks for a series of files of type .jpg, .jpeg, or .png
    in a subdirectory "input" and then merges them together using the
    FocusStack module.  The output is put in the file merged.png


    Author:     Charles McGuinness (charles@mcguinness.us)
    Copyright:  Copyright 2015 Charles McGuinness
    License:    Apache License 2.0

"""


def remove_images_having_wrong_type(image_files):
    for img in image_files:
        if img.split('.')[-1].lower() not in ['jpg', 'jpeg', 'png']:
            image_files.remove(img)


def stackHDRs(image_files):
    images = ImageReader(image_files)
    focusimages = images.read()
    merged = FocusStack.focus_stack(focusimages)
    cv2.imwrite("merged.png", merged)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == 'raw':
        image_files = sorted(os.listdir('input'))
        remove_images_having_wrong_type(image_files)
    else:
        image_files = sorted(os.listdir('input'))
        remove_images_having_wrong_type(image_files)

    stackHDRs(image_files)
    print('Done!')
