#!/usr/bin/env python3

from PIL import Image
import os

folder = "/Users/evemwangi/python_andthe_os/capstone/images"
new_folder = "/Users/evemwangi/python_andthe_os/capstone/images_new"

try:
    os.makedirs(new_folder)
except FileExistsError:
    # directory already exists
    print("Folder already exists")
    pass

for infile in os.listdir(folder):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"

    print("infile IS::", infile)
    print("outfile IS::", outfile)

    with Image.open(folder + "/" + infile) as im:
        print("image in process is:", infile)
        print(new_folder + "/" + outfile)
        print("OLD mode is: " + im.mode)
        im = im.convert('RGB')
        print("new mode is: " + im.mode)
        im.rotate(90).resize((128,128)).save(new_folder + "/" + outfile)

    """if infile != outfile:
        try:
            with Image.open(infile) as im:
                print("image in process is:", infile)
                print(new_folder + "/" + outfile)
                im.rotate(90).resize((128,128)).save(new_folder + "/" + outfile)
        except:
            print("Cannot convert image", infile)"""

"""
im = Image.open("/Users/evemwangi/python_andthe_os/capstone/doe.jpg")
# im.rotate(45).show()
im.rotate(180).resize((640,480)).save("/Users/evemwangi/python_andthe_os/capstone/flipped_and_resized.jpg")

new_im = im.resize((640,480))
#new_im.save("/Users/evemwangi/python_andthe_os/capstone/resized.jpg")
"""

"""
Iterate through each file in the folder
For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format
Use a nano editor for this purpose. You can name the file however you'd like. And make sure to save the updated images in the folder: /opt/icons/

"""