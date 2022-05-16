import cv2
from . import utils
from matplotlib import image

def euclidianDistance(image_1_path, image_2_path):
    image_1, image_2 = utils.load_images(image_1_path, image_2_path)
    histogram_1 = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    histogram_2 = cv2.calcHist([image_2], [0], None, [256], [0, 256])

    c1 = 0
    i = 0
    while i < len(histogram_1) and i < len(histogram_2):
        c1 += (histogram_1[i] - histogram_2[i]) ** 2
        i += 1
    c1 = c1 ** 0.5
    return c1

def templateMatching(image_1_path, image_2_path):
    image_1, image_2 = utils.load_images(image_1_path, image_2_path)
    image_1 = cv2.GaussianBlur(image_1, (5, 5), 0)
    image_2 = cv2.GaussianBlur(image_2, (5, 5), 0)
    
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED',     'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    similarity = cv2.matchTemplate(image_1, image_2, cv2.TM_CCOEFF_NORMED)
    return similarity

    