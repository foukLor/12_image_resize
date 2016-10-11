import argparse
import os
from PIL import Image


def resize_image(path_to_original, **kwargs):
    im = Image.open(path_to_original)
    width = kwargs.get('width')
    height = kwargs.get('height')
    scale = kwargs.get('scale')
    output = kwargs.get('output')
    if scale is not None:
        scale = int(scale)
        new_size = (int(im.width*scale), int(im.height*scale))
        im = im.resize(new_size)
        if (height or width) is not None:
            exit(1)
        else:
            return im
    if width is not None and height is not None:
        width = int(width)
        height = int(height)
        if int(height/im.height) != int(im.width/width):
            exit("your size is not adequate")
    if height is None and width is not None:
        width = int(width)
        height = int(im.width/width*im.height)
    if width is None and height is not None:
        height = int(height)
        width = int(height/im.height*im.width)
    if width is None and height is None:
        exit("please input width or heigth") 
    im = im.resize((width, height))
    return im


def save_image(new_image, path_to_save):
    print("saving to {0}".format(path_to_save))
    new_image.save(path_to_save)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_img",
             help="display a path to image, that you want to resize")
    parser.add_argument("--width", help="width of the image")
    parser.add_argument("--height", help="height of the image")
    parser.add_argument("--scale", help="scale of the resizing")
    parser.add_argument("--output", help="output path")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    arguments = parse_arguments()
    path_save = arguments.output
    img = resize_image(arguments.path_to_img, scale=arguments.scale,
                 width=arguments.width, height=arguments.height)
    if path_save is None:
        name = os.path.splitext(os.path.basename(arguments.path_to_img))
        path_save = "{0}__{1}x{2}.jpg".format(name[0], img.width, img.height)
    save_image(img, path_save)
