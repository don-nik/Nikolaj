#!/usr/bin/python
from PIL import Image
import os, sys

filepath = "/path/to/file"
dirs = os.listdir( filepath )

size = (384,128)

def resize():
    """
    This function rescales an image file into desired pixel dimensions
    """
    for item in dirs:
        if os.path.isfile(os.path.join(filepath,item)):
            im = Image.open(os.path.join(filepath,item))
            width, height = im.size
            if im.size == (477,159): 
                string = os.path.splitext(os.path.join(filepath,item))
                imResize = im.resize(size, Image.ANTIALIAS)
                imResize.save(f + '_rescaled.png', 'PNG', quality=90)

resize()