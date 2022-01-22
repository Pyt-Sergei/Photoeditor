from PIL import Image, ImageFilter
import numpy as np
import cv2


def to_white_black(path):
    with Image.open(path) as img:
        img.convert('L').save(path)


def to_blue(path):
    with Image.open(path) as img:
        img = np.array(img)
        img[:, :, 2] = 255
        img = Image.fromarray(img)
        img.save(path)


def negative(path):
    with Image.open(path) as img:
        img_array = 255 - np.array(img)
        img = Image.fromarray(img_array)
        img.save(path)


def blur(path, radius=5):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.GaussianBlur(radius))
        img.save(path)


def contour(path):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.CONTOUR)
        img.save(path)


def detail(path):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.DETAIL)
        img.save(path)


def emboss(path):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.EMBOSS)
        img.save(path)


def edge_enhance(path):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        img.save(path)


def find_edges(path):
    with Image.open(path) as img:
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save(path)


def cartoonize(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 1)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9, 9)

    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    ret, label, center = cv2.kmeans(data, 9, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result_img = center[label.flatten()]
    result_img = result_img.reshape(img.shape)

    color = cv2.bilateralFilter(result_img, d=7, sigmaColor=200, sigmaSpace=200)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imwrite(path, cartoon)


def oil_painting(path, dst=7):
    img = cv2.imread(path)

    oil_picture = cv2.xphoto.oilPainting(img, dst, 1)
    cv2.imwrite(path, oil_picture)


filters_dict = {
    'white-black': to_white_black,
    'blue': to_blue,
    'negative': negative,
    'blur': blur,
    'contour': contour,
    'detail': detail,
    'emboss': emboss,
    'edge_enhance': edge_enhance,
    'find_edges': find_edges,
    'cartoonize': cartoonize,
    'oil_painting': oil_painting
}
