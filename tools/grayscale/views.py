import numpy as np
import cv2
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,HttpResponse,redirect
import os
def takePhoto(request):
    if request.method=="POST":
        image=request.FILES.get("userimage")
        #filesystestorage ka object banaya
        fs=FileSystemStorage()
        #file ko save karwaya
        filename=fs.save(image.name,image)
        #jaha file save hui uska address nikala
        filepath=fs.path(filename)
        #address file ko cv2 mein read karwaaya
        data=cv2.imread(filepath)

        #grayscale mein 
        # convert kiya
        data2=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
        #naya address banaya taki grayscale photo ko save kiya ja sake
        path=os.path.join(fs.location,"../../static/gray")
        #naya filename banaya with extension explicitly
        newfilename=f"gray_{filename}.jpg"

        #new address or filename ko join kiya
        completePath=os.path.join(path,newfilename)

        #grayscale matrix(2d) array ko image mein convert kiya
        cv2.imwrite(completePath,data2)
    
        return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'takephoto'})
    else:
        return render(request,"user.html")

   #compress Image

def compressing(request):
        if request.method=='POST':
            image=request.FILES.get("compressimg")
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            filepath=fs.path(filename)
            data=cv2.imread(filepath)
            
            #compress image function
            data2=data.astype("uint8")
            path=os.path.join(fs.location,"../../static/compress")
            newfilename=f"comp_{filename}.jpg"
            completePath=os.path.join(path,newfilename)
            cv2.imwrite(completePath,data2)
            print(data2)
            return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'compress'})
        else:
            return render(request,"user.html")
        
def resizing(request):

    if request.method=='POST':
            image=request.FILES.get("resizing")
            size=float(request.POST.get("size"))
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            filepath=fs.path(filename)
            data=cv2.imread(filepath)
            print(size)
            
            #resizeing image function
            data2=cv2.resize(data,None,fx=size,fy=size)           
            path=os.path.join(fs.location,"../../static/resize")
            newfilename=f"resize_{filename}.jpg"
            completePath=os.path.join(path,newfilename)
            cv2.imwrite(completePath,data2)
            print(data2)
            return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'resizing'})
    else:
            return render(request,"user.html")
        
          
def rotate(request):
      if request.method=='POST':
           image=request.FILES.get("rotating")
           degree=int(request.POST.get("degree"))
           fs=FileSystemStorage()
           filename=fs.save(image.name,image)
           filepath=fs.path(filename)
           data=cv2.imread(filepath)
           print(degree)

           #function rotate
           if degree==0:
                rotate=data
           elif degree==90:
                rotate=cv2.rotate(data,cv2.ROTATE_90_CLOCKWISE)
           elif degree==180:
                rotate=cv2.rotate(data,cv2.ROTATE_180)
           elif degree==270:
                rotate=cv2.rotate(data,cv2.ROTATE_90_COUNTERCLOCKWISE)

           data2=rotate
           path=os.path.join(fs.location,"../../static/rotate")
           newfilename=f"rotate_{filename}.jpg"
           completePath=os.path.join(path,newfilename)
           cv2.imwrite(completePath,data2)
           print(data2)
           return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'rotatephoto'})
      else:
           return render(request,"user.html")

def signin(request):
     return render(request,'signin.html')

ptr1 = []
count = 0
data = None
filepath = ""
filename = ""

def myclick(event, x, y, flags, param):
    global ptr1, count, data,cropfilename

    height = 250
    width = 350

    if event == cv2.EVENT_LBUTTONDOWN:

        count += 1

        # Restart if 5th click happens
        if count == 5:
            ptr1 = []
            count = 1
            data = cv2.imread(filepath)

        # draw circle
        cv2.circle(data, (x, y), 3, (0, 255, 0), -1)

        # store point
        ptr1.append((x, y))

        # When 4 points selected -> crop
        if count == 4:
            cv2.line(data, ptr1[0], ptr1[1], (0, 255, 0), 2)
            cv2.line(data, ptr1[1], ptr1[2], (0, 255, 0), 2)
            cv2.line(data, ptr1[2], ptr1[3], (0, 255, 0), 2)
            cv2.line(data, ptr1[3], ptr1[0], (0, 255, 0), 2)

            # Target rectangle points
            ptr2 = [
                [0,0], [0,height], [width,height], [width,0]
            ]

            # Perspective transform
            matrix = cv2.getPerspectiveTransform(
                src=np.float32(ptr1),
                dst=np.float32(ptr2)
            )

            cropped = cv2.warpPerspective(data, matrix, (width, height))

            # Save file
            fs = FileSystemStorage()
            save_path=os.path.join(fs.location,"../../static/crop")
            cropfilename = f"crop_{filename}.jpg"
            final_path = os.path.join(save_path, cropfilename)
            cv2.imwrite(final_path, cropped)
            #cv2.imshow("Cropped Result", cropped)

            print("Cropping Done!")


def Crop(request):
    global filename, filepath, data, ptr1, count

    ptr1 = []
    count = 0

    if request.method == "POST":
        image = request.FILES.get("crop")
        fs = FileSystemStorage()

        filename = fs.save(image.name, image)
        filepath = fs.path(filename)

        data = cv2.imread(filepath)

        cv2.namedWindow("Crop Tool")
        cv2.setMouseCallback("Crop Tool", myclick)

        while True:
            cv2.imshow("Crop Tool", data)
            if cv2.waitKey(20) == ord('a'):  # press 'a' to exit
                break

        cv2.destroyAllWindows()

        return render(request,'user.html',{'lelo':cropfilename, 'tool_name': 'crop'}) 

    return render(request, 'user.html')
