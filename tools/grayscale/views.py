import numpy as np
import os
import cv2
from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
from .services import process_grayscale
from .services import process_resize
from .services import process_rotate
from .services import process_compress
from .services import process_brightness
from .services import process_contrast
from .services import process_blur
from .services import process_convert
from .services import process_watermark

def takePhoto(request):

    if request.method == "POST":

        image = request.FILES.get("userimage")

        output_file = process_grayscale(image)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "takephoto"}
        )

    return render(request, "user.html")


# compress Image


def compressing(request):

    if request.method == "POST":

        image = request.FILES.get("compressimg")

        output_file = process_compress(image)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "compress"}
        )

    return render(request, "user.html")


def resizing(request):

    if request.method == "POST":

        image = request.FILES.get("resizing")

        size = float(request.POST.get("size"))

        output_file = process_resize(image, size)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "resizing"}
        )

    return render(request, "user.html")


def rotate(request):

    if request.method == "POST":

        image = request.FILES.get("rotating")

        degree = int(request.POST.get("degree"))

        output_file = process_rotate(image, degree)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "rotatephoto"}
        )

    return render(request, "user.html")



def myclick(event, x, y, flags, param):
    global ptr1, count, data, cropfilename, original

    if event == cv2.EVENT_LBUTTONDOWN:

        count += 1
        
        if count == 5:
            ptr1 = []
            count = 1
            data = original.copy()

        cv2.circle(data, (x, y), 3, (0, 255, 0), -1)

        ptr1.append((x, y))

        if count == 4:

            width = max(
            np.linalg.norm(np.array(ptr1[0]) - np.array(ptr1[3])),
            np.linalg.norm(np.array(ptr1[1]) - np.array(ptr1[2])))

            height = max(
                np.linalg.norm(np.array(ptr1[0]) - np.array(ptr1[1])),
                np.linalg.norm(np.array(ptr1[3]) - np.array(ptr1[2])))
            
            width = int(width)
            height = int(height)

            cv2.line(data, ptr1[0], ptr1[1], (0, 255, 0), 2)
            cv2.line(data, ptr1[1], ptr1[2], (0, 255, 0), 2)
            cv2.line(data, ptr1[2], ptr1[3], (0, 255, 0), 2)
            cv2.line(data, ptr1[3], ptr1[0], (0, 255, 0), 2)

            ptr2 = [[0, 0], [0, height], [width, height], [width, 0]]

            matrix = cv2.getPerspectiveTransform(
                src=np.float32(ptr1), dst=np.float32(ptr2)
            )

            cropped = cv2.warpPerspective(original, matrix, (width, height))

            # Save file
            fs = FileSystemStorage()
            save_path = os.path.join(fs.location, "../../static/crop")
            cropfilename = f"crop_{filename}.jpg"
            final_path = os.path.join(save_path, cropfilename)
            cv2.imwrite(final_path, cropped)

            print("Cropping Done!")


def Crop(request):
    global filename, filepath, cropfilename, data, ptr1, count, original

    ptr1 = []
    count = 0
    cropfilename=None

    if request.method == "POST":
        image = request.FILES.get("crop")
        fs = FileSystemStorage()

        filename = fs.save(image.name, image)
        filepath = fs.path(filename)

        original = cv2.imread(filepath)
        data = original.copy()
        cv2.namedWindow("Crop Tool")
        cv2.setMouseCallback("Crop Tool", myclick)

        while True:
            cv2.imshow("Crop Tool", data)
            if cv2.waitKey(20) == ord("a"):
                break

        cv2.destroyAllWindows()
        if cropfilename:
            return render(request, "user.html", {"lelo": cropfilename, "tool_name": "crop"})

    return render(request, "user.html")


def brightness(request):

    if request.method == "POST":

        image = request.FILES.get("brightness")

        brightness_value = int(request.POST.get("brightness_value"))

        output_file = process_brightness(image, brightness_value)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "brightness"}
        )

    return render(request, "user.html")


def contrast(request):

    if request.method == "POST":

        image = request.FILES.get("contrast")

        contrast_value = float(request.POST.get("contrast_value"))

        output_file = process_contrast(image, contrast_value)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "contrast"}
        )

    return render(request, "user.html")


def blur(request):

    if request.method == "POST":

        image = request.FILES.get("blur")

        output_file = process_blur(image)

        return render(request, "user.html", {"lelo": output_file, "tool_name": "blur"})

    return render(request, "user.html")


def convert_file(request):

    if request.method == "POST":

        image = request.FILES.get("convert")

        target_format = request.POST.get("target_format")

        output_file = process_convert(image, target_format)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "convert"}
        )

    return render(request, "user.html")


def watermark(request):

    if request.method == "POST":

        image = request.FILES.get("watermark")

        watermark_text = request.POST.get("watermark_text")

        output_file = process_watermark(image, watermark_text)

        return render(
            request, "user.html", {"lelo": output_file, "tool_name": "watermark"}
        )

    return render(request, "user.html")
