import argparse
import os
from PIL import Image



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_img",
             help="display a path to image, that you want to resize")
    parser.add_argument("--width", help="width of the image")
    parser.add_argument("--height", help="height of the image")
    parser.add_argument("--scale", help="scale of the resizing")
    parser.add_argument("--output", help="output path")
    return parser.parse_args()


def resize_image(arguments):
    image = Image.open(arguments.path_to_img)
    if arguments.output is not None:
        path_to_img = os.path.join(arguments.output, os.path.split(arguments.path_to_img)[1])
    else:
        path_to_img = arguments.path_to_img
    width = arguments.width
    height = arguments.height
    scale = arguments.scale
    if scale is not None:
        if width or height is not None:
            print("Please use one type of resize.")
            exit()
        new_width, new_height = get_new_image_size_by_scale(image, scale)
    else:
        new_width, new_height = get_new_image_size_by_parametrs(image, width, height)
    resize_and_save_image(image, new_width, new_height, path_to_img)


def get_new_image_size_by_scale(image, scale):
    scale = int(scale)
    new_size = (int(image.width*scale), int(image.height*scale))
    return new_size


def get_new_image_size_by_parametrs(image, width, height):
    return (int(width or image.width), int(height or image.height))


def resize_and_save_image(image, width, height, path_to_save):
    print("saving image to {0}".format(path_to_save))
    new_image = image.resize((width, height))
    new_image.save(get_new_image_name(width, height, path_to_save))
    print("resizing finished")

def get_new_image_name(width, height, full_path_to_img):
    image_path, image_format = os.path.splitext(full_path_to_img)
    new_full_name = "{0}__{1}x{2}{3}".format(image_path,width, height, image_format)
    return new_full_name



if __name__ == '__main__':
    arguments = parse_arguments()
    path_save = arguments.output
    img = resize_image(arguments)
