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

def get_image_by_path(path_to_img):
    return Image.open(path_to_img)


def resize_image(arguments):
    image = get_image_by_path(arguments.path_to_img)
    if arguments.scale is not None:
        if arguments.width or arguments.height is not None:
            return None
        new_width, new_height = get_new_image_size_by_scale(image, arguments.scale)
    else:
        new_width, new_height = get_new_image_size_by_parametrs(image, arguments.width, arguments.height)
    print_warning_before_resized()
    new_image = image.resize((new_width, new_height))
    return new_image


def print_warning_before_resized():
    print("Your image will be resized")

def print_new_image_name(image_name):
    print("New name - {0}".format(image_name))


def get_new_image_size_by_scale(image, scale):
    scale = int(scale)
    new_size = (int(image.width*scale), int(image.height*scale))
    return new_size


def get_new_image_size_by_parametrs(image, width, height):
    return (int(width or image.width), int(height or image.height))


def save_image(image, path_to_save):
    new_path_to_save = get_new_image_name(image.width, image.height, path_to_save)
    image.save(new_path_to_save)
    print_new_image_name(new_path_to_save)


def get_new_image_name(width, height, full_path_to_img):
    image_path, image_format = os.path.splitext(full_path_to_img)
    new_full_name = "{0}__{1}x{2}{3}".format(image_path,width, height, image_format)
    return new_full_name



if __name__ == '__main__':
    arguments = parse_arguments()
    if arguments.path_to_img is None:
        print("You forgot about path to the image")
        exit()
    if arguments.output is not None:
        path_to_img = os.path.join(arguments.output, os.path.split(arguments.path_to_img)[1])
    else:
        path_to_img = arguments.path_to_img
    img = resize_image(arguments)
    if img is None:
        print("Please use one type of resize.")
        exit()
    save_image(img, path_to_img)