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

    width = arguments.width
    height = arguments.height
    scale = arguments.scale
    if scale is not None:
        if width or height is not None:
            print("Please use one type of resize.")
            return
        new_width, new_height = get_new_image_size_by_scale(image, scale)
    else:
        new_width, new_height = get_new_image_size_by_parametrs(image, width, height)
    new_image = image.resize((new_width, new_height))
    return new_image


def get_new_image_size_by_scale(image, scale):
    scale = int(scale)
    new_size = (int(image.width*scale), int(image.height*scale))
    return new_size


def get_new_image_size_by_parametrs(image, width, height):
    return (int(width or image.width), int(height or image.height))


def save_image(image, path_to_save):
    print("saving image to {0}".format(path_to_save))
    new_path_to_save = get_new_image_name(image.width, image.height, path_to_save)
    image.save(new_path_to_save)
    print("resizing finished \nnew image was saved ")


def get_new_image_name(width, height, full_path_to_img):
    image_path, image_format = os.path.splitext(full_path_to_img)
    new_full_name = "{0}__{1}x{2}{3}".format(image_path,width, height, image_format)
    return new_full_name



if __name__ == '__main__':
    arguments = parse_arguments()
    if arguments.output is not None:
        path_to_img = os.path.join(arguments.output, os.path.split(arguments.path_to_img)[1])
    else:
        path_to_img = arguments.path_to_img
    img = resize_image(arguments)
    if img is None:
        exit()
    save_image(img, path_to_img)