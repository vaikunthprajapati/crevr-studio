![Crevr_Thumbnail](Crevr_Thumbnail.png)
<img src="Crevr_Thumbnail.png" width="100%">

# CREVR STUDIO

A web-based image processing platform built with Django and OpenCV that allows users to perform common computer vision and image manipulation operations directly from the browser.

---

## Overview

CREVR STUDIO was developed to explore practical computer vision concepts using OpenCV while building a complete full-stack application with Django.

The platform provides a collection of image processing tools through a clean web interface, enabling users to upload, transform, and download images without requiring any external software.

---

## Features

* Grayscale Conversion
* Image Compression
* Image Resizing
* Image Rotation
* Perspective Crop Tool
* Brightness Adjustment
* Contrast Adjustment
* Gaussian Blur
* Image Format Conversion (JPG, PNG, WEBP)
* Watermark Generation

---

## Technologies Used

### Backend

* Python
* Django
* OpenCV
* NumPy

### Frontend

* HTML5
* CSS3
* JavaScript

### Storage

* Django FileSystemStorage

---

## Computer Vision Concepts Demonstrated

This project implements several core OpenCV operations, including:

* Color Space Conversion
* Geometric Transformations
* Perspective Transformations
* Image Filtering
* Pixel Intensity Manipulation
* File Format Encoding
* Image Compression Techniques

---

## Project Structure

```text
CREVR_TOOL_MAIN
│
├── screenshots/
├── tools/
│   ├── grayscale/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── ...
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Status

Project completed and maintained for learning and portfolio purposes.

## Installation

```bash
git clone https://github.com/your-username/crevr-studio.git

cd crevr-studio/tools

python -m venv venv

venv\Scripts\activate

pip install -r ../requirements.txt

python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

## Future Improvements

* Drag-and-drop uploads
* Side-by-side image comparison
* Batch image processing
* User authentication
* Cloud deployment

---

## Author

**Vaikunth Prajapati**

LinkedIn:
https://www.linkedin.com/in/vaikunthprajapati
