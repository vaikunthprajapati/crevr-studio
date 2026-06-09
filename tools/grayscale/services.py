import os
import cv2
from django.core.files.storage import FileSystemStorage
from .image_utils import (
    convert_to_grayscale,
    resize_image,
    rotate_image,
    compress_image,
    crop_perspective,
    adjust_brightness,
    adjust_contrast,
    apply_blur,
    convert_format,
    add_watermark,
)


def process_grayscale(uploaded_file):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    gray_image = convert_to_grayscale(filepath)

    save_path = os.path.join(fs.location, "../../static/gray")

    new_filename = f"gray_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, gray_image)

    return new_filename


def process_resize(uploaded_file, scale):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    resized_image = resize_image(filepath, scale)

    save_path = os.path.join(fs.location, "../../static/resize")

    new_filename = f"resize_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, resized_image)

    return new_filename


def process_rotate(uploaded_file, degree):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    rotated_image = rotate_image(filepath, degree)

    save_path = os.path.join(fs.location, "../../static/rotate")

    new_filename = f"rotate_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, rotated_image)

    return new_filename


def process_compress(uploaded_file):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    compressed_image = compress_image(filepath)

    save_path = os.path.join(fs.location, "../../static/compress")

    new_filename = f"comp_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, compressed_image)

    return new_filename


def process_brightness(uploaded_file, brightness):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    bright_image = adjust_brightness(filepath, brightness)

    save_path = os.path.join(fs.location, "../../static/brightness")

    os.makedirs(save_path, exist_ok=True)

    new_filename = f"bright_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, bright_image)

    return new_filename


def process_contrast(uploaded_file, contrast):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    contrast_image = adjust_contrast(filepath, contrast)

    save_path = os.path.join(fs.location, "../../static/contrast")

    os.makedirs(save_path, exist_ok=True)

    new_filename = f"contrast_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, contrast_image)

    return new_filename


def process_blur(uploaded_file):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    blurred_image = apply_blur(filepath)

    save_path = os.path.join(fs.location, "../../static/blur")

    os.makedirs(save_path, exist_ok=True)

    new_filename = f"blur_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, blurred_image)

    return new_filename


def process_convert(uploaded_file, target_format):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    image = convert_format(filepath)

    save_path = os.path.join(fs.location, "../../static/converted")

    os.makedirs(save_path, exist_ok=True)

    file_name_without_ext = os.path.splitext(filename)[0]

    new_filename = f"converted_{file_name_without_ext}.{target_format}"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, image)

    return new_filename


def process_watermark(uploaded_file, watermark_text):

    fs = FileSystemStorage()

    filename = fs.save(uploaded_file.name, uploaded_file)

    filepath = fs.path(filename)

    watermarked_image = add_watermark(filepath, watermark_text)

    save_path = os.path.join(fs.location, "../../static/watermark")

    os.makedirs(save_path, exist_ok=True)

    new_filename = f"watermark_{filename}.jpg"

    final_path = os.path.join(save_path, new_filename)

    cv2.imwrite(final_path, watermarked_image)

    return new_filename
