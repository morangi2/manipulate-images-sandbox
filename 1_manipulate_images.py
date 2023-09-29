#!/usr/bin/env python3

from PIL import Image
import os

folder = "/~/images"
new_folder = "/~/images_new"

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
im = Image.open("/~/doe.jpg")
# im.rotate(45).show()
im.rotate(180).resize((640,480)).save("/~/flipped_and_resized.jpg")

new_im = im.resize((640,480))
#new_im.save("/~/resized.jpg")
"""
