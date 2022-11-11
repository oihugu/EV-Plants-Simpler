import cv2
from . import utils
from matplotlib import image
from skimage.metrics import structural_similarity as ssim
from imed import distance as imed_distance
import numpy as np
from multiprocessing import Pool


def euclidianDistance(image_1_path, image_2_path):
    image_1, image_2 = utils.load_images(image_1_path, image_2_path)
    with Pool(5) as p:
        histogram_1, histogram_2 = p.map(cv2.calcHist, [([image_1], [0], None, [256], [0, 256]), ([image_2], [0], None, [256], [0, 256])])

    c1 = 0
    i = 0
    while i < len(histogram_1) and i < len(histogram_2):
        c1 += (histogram_1[i] - histogram_2[i]) ** 2
        i += 1
    c1 = c1 ** 0.5
    return c1

def templateMatching(image_1_path, image_2_path):
    image_1, image_2 = utils.load_images(image_1_path, image_2_path)
    with Pool(5) as p:
        image_1, image_2 = p.map(cv2.GaussianBlur, [(image_1, (5, 5), 0), (image_2, (5, 5), 0)])   
    
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    similarity = cv2.matchTemplate(image_1, image_2, cv2.TM_CCOEFF_NORMED)
    return similarity

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def mse_ssim(image_1_path, image_2_path):
    imageA, imageB = utils.load_images(image_1_path, image_2_path)
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return m, s

def wrap_swift(img):
    _ ,desc = sift.detectAndCompute(img,None)
    return desc

def sift(image_1_path, image_2_path):
        img_1 = cv2.imread(image_1_path)
        img_2 = cv2.imread(image_2_path)

        with Pool(8) as p:
            desc_1, desc_2 = p.map(wrap_swift, [img_1, img_2])

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc_1, desc_2, k=2)
        return matches

def imed(image_1_path, image_2_path):
    img_1 = cv2.imread(image_1_path)
    img_2 = cv2.imread(image_2_path)
    img_1 = cv2.resize(img_1, (250,250))
    img_2 = cv2.resize(img_2, (250,250))
    return imed_distance(img_1, img_2, sigma=1)

