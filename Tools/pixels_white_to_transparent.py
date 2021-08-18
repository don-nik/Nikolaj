#!/usr/bin/python
from PIL import Image

"""
This file converts all white pixels in an image to transparent pixels with an alpha value
"""

img = Image.open("old_image.png")
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 255))
    else:
        newData.append(item)

img.putdata(newData)
img.save("new_image.png", "PNG")
