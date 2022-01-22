from PIL import Image
import numpy as np


def resize(path, size, *args, **kwargs):
    with Image.open(path) as img:
        img = img.resize(size, *args, resample=Image.BILINEAR, **kwargs)
        img.save(path)


def scale(path, size=None, scaling=1, *args, **kwargs):
    with Image.open(path) as img:
        if size is not None:
            max_width, max_height = size[0], size[1]

            ratio = min(max_width / img.width, max_height / img.height)
            width = int(img.width * ratio)
            height = int(img.height * ratio)
        else:
            width, height = int(img.width * scaling), int(img.height * scaling)

        img = img.resize((width, height), *args, resample=Image.BILINEAR, **kwargs)
        img.save(path)


def rotate(path, angle=0, *args, **kwargs):
    with Image.open(path) as img:
        img = img.rotate(angle, *args, expand=True, **kwargs)
        img.save(path)


def reverse(path):
    with Image.open(path) as img:
        img = np.fliplr(img)
        img = Image.fromarray(img)
        img.save(path)


#  The box is a 4-tuple defining the left, upper, right, and lower distances
def crop(path, box):
    with Image.open(path) as img:
        left, upper, right, lower = box
        right = img.width - right
        lower = img.height - lower
        box = left, upper, right, lower
        img = img.crop(box)
        img.save(path)
