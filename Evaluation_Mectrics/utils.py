import cv2

def load_images(image_1_path, image_2_path):
    image_1 = cv2.imread(image_1_path)
    image_2 = cv2.imread(image_2_path)
    image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
    return image_1, image_2