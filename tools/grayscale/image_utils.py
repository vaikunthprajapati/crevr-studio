import cv2
import numpy as np


def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray_image


def resize_image(image_path, scale):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    resized_image = cv2.resize(image, None, fx=scale, fy=scale)

    return resized_image


def rotate_image(image_path, degree):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    if degree == 0:
        rotated_image = image

    elif degree == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif degree == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    elif degree == 270:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    else:
        rotated_image = image

    return rotated_image


def compress_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    compressed_image = image.astype("uint8")

    return compressed_image


def crop_perspective(image_path, points, width=350, height=250):

    image = cv2.imread(image_path)

    pts = np.array(ptr1, dtype="float32")

    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    top_left = pts[np.argmin(s)]
    bottom_right = pts[np.argmax(s)]
    top_right = pts[np.argmin(diff)]
    bottom_left = pts[np.argmax(diff)]

    ordered = np.array([top_left, top_right, bottom_right, bottom_left],dtype="float32")

    matrix = cv2.getPerspectiveTransform(
        src=np.float32(points),
        dst=np.float32([[0, 0], [0, height], [width, height], [width, 0]]),
    )

    cropped = cv2.warpPerspective(image, matrix, (width, height))

    return cropped


def adjust_brightness(image_path, brightness):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    bright_image = cv2.convertScaleAbs(image, alpha=1.0, beta=brightness)

    return bright_image


def adjust_contrast(image_path, contrast):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    contrast_image = cv2.convertScaleAbs(image, alpha=contrast, beta=0)

    return contrast_image


def apply_blur(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    return blurred_image


def convert_format(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    return image


def add_watermark(image_path, watermark_text):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    height, width = image.shape[:2]

    cv2.putText(image,watermark_text,(width - 250, height - 20),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255),2,cv2.LINE_AA,)

    return image
