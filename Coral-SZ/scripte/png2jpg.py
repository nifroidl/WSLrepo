"""Tool for converting images inside a directory from .png-format to .jpg-format.
"""
import os
import glob
from PIL import Image

from scripte.tools.utilities import colors, symbols

def png2jpg(images_path, export_path, textOutput):

    os.makedirs(export_path, exist_ok=True)

    image_count = 0

    # convert images
    for file in sorted(glob.glob(f"{images_path}/*.png")) :
        # open png-file
        img = Image.open(file)
        
        # convert file to RGB format
        img = img.convert('RGB')

        # Get filename without .png extension and set output path for .jpg file
        file = os.path.basename(file)
        filename, extension = os.path.splitext(file)
        outputFile = os.path.join(export_path, filename + '.jpg')

        # save .jpg file
        img.save(outputFile)
        textOutput(f"\t{file} \t{symbols.ARROW} \t{filename + '.jpg'}")
        image_count += 1

    return 1
